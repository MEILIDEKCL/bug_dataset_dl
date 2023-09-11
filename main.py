import time

import json
import requests
from bs4 import BeautifulSoup


def main():
    url_dict = json.load(open("dataset.json", 'r'))
    failed_url = []
    result = {}
    success_url = []

    for project in url_dict:
        with open(project, 'a') as f:
            print(f"开始爬取项目: {project}")
            tmp_result = set()
            url_list = url_dict[project]
            for url in url_list:
                print(f"开始爬取url: {url}")
                time.sleep(5)
                # 休眠一会儿再爬
                re_res, yes = get_request(url)
                if yes:
                    # 如果成功就把结果加入到集合中
                    tmp_result.update(re_res)
                else:
                    # 如果失败的话就加入到失败队列中
                    failed_url.append(url)
                print(f"当前结果是:{re_res}")
                print(f"当前总的结果是:{tmp_result}")
                for rr in re_res:
                    f.write(rr + "  ")
                f.write("\n")
            with open(f"{project}.json", 'w') as file:
                # 把集合结果写入到json中
                json.dump({project: tmp_result}, file)

    with open("failed_url.json", 'w') as f:
        json.dump(failed_url, f)


def sub_tensorflow_main():
    url_dict = json.load(open("dataset.json", 'r'))
    tensorflow_list = url_dict['TensorFlow']
    success_url_list = []
    with open('tensorflow_success_url.txt', 'r') as f:
        ul = f.readline()
        success_url_list.append(ul)
    for url in tensorflow_list:
        if url in success_url_list:
            # 如果成功就跳过
            print(f"跳过当前url:{url}")
            continue
        # 否则就爬取
        print(f"开始爬取url: {url}")
        time.sleep(5)
        re_res, yes = get_request(url)
        if yes:
            # 把成功的url写入到文件中
            with open('tensorflow_success_url.txt', 'a') as f:
                f.write(url)
                f.write('\n')
            with open('tensorflow_result.txt', 'a') as f:
                for i in re_res:
                    f.write(i)
                    f.write('\n')
        print(f"当前结果是:{re_res}")


def sub_pytorch_main():
    url_dict = json.load(open("dataset.json", 'r'))
    tensorflow_list = url_dict['PyTorch']
    success_url_list = []
    with open('pytorch_success_url.txt', 'r') as f:
        ul = f.readline()
        success_url_list.append(ul)
    for url in tensorflow_list:
        if url in success_url_list:
            # 如果成功就跳过
            print(f"跳过当前url:{url}")
            continue
        # 否则就爬取
        print(f"开始爬取url: {url}")
        time.sleep(5)
        re_res, yes = get_request(url)
        if yes:
            # 把成功的url写入到文件中
            with open('pytorch_success_url.txt', 'a') as f:
                f.write(url)
                f.write('\n')
            with open('pytorch_result.txt', 'a') as f:
                for i in re_res:
                    f.write(i)
                    f.write('\n')
        print(f"当前结果是:{re_res}")


def sub_mxnet_main():
    url_dict = json.load(open("dataset.json", 'r'))
    mxnet_list = url_dict['MXNet']
    success_url_list = []
    with open('mxnet_success_url.txt', 'r') as f:
        ul = f.readline()
        success_url_list.append(ul)
    for url in mxnet_list:
        if url in success_url_list:
            # 如果成功就跳过
            print(f"跳过当前url:{url}")
            continue
        # 否则就爬取
        print(f"开始爬取url: {url}")
        time.sleep(5)
        re_res, yes = get_request(url)
        if yes:
            # 把成功的url写入到文件中
            with open('mxnet_success_url.txt', 'a') as f:
                f.write(url)
                f.write('\n')
            with open('mxnet_result.txt', 'a') as f:
                for i in re_res:
                    f.write(i)
                    f.write('\n')
        print(f"当前结果是:{re_res}")


def sub_dl4j_main():
    url_dict = json.load(open("dataset.json", 'r'))
    dl4j_list = url_dict['DL4J']
    success_url_list = []
    with open('dl4j_success_url.txt', 'r') as f:
        ul = f.readline()
        success_url_list.append(ul)
    for url in dl4j_list:
        if url in success_url_list:
            # 如果成功就跳过
            print(f"跳过当前url:{url}")
            continue
        # 否则就爬取
        print(f"开始爬取url: {url}")
        time.sleep(5)
        re_res, yes = get_request(url)
        if yes:
            # 把成功的url写入到文件中
            with open('dl4j_success_url.txt', 'a') as f:
                f.write(url)
                f.write('\n')
            with open('dl4j_result.txt', 'a') as f:
                for i in re_res:
                    f.write(i)
                    f.write('\n')
        print(f"当前结果是:{re_res}")


def get_request(url: str):
    access_token = 'xxxxxxxxxx'  # 你的github的token
    headers = {'Authorization': f'token {access_token}'}
    proxy = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890'
    }
    response = requests.get(url, headers=headers, proxies=proxy)
    res = set()
    if response.status_code != 200:
        print("这次爬虫失败了")
        return res, False
    print("这次爬虫成功了，正在处理内容")
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获得所有的li标签
    ul_tags = soup.find_all('ul', attrs={'class': "ActionList ActionList--subGroup"})
    for ul in ul_tags:
        ul_list = ul.text.split()
        # 判断内部的数据是否为cc结尾或者py结尾
        for context in ul_list:
            if ('.cc' in context or '.py' in context) and '/' not in context:
                res.add(context)
    return res, True


def get_json_data() -> dict:
    with open("dataset.json", 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    sub_dl4j_main()
    # get_request("https://github.com/tensorflow/tensorflow/pull/52276/files")

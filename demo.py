import requests

url = 'http://127.0.0.1:3000/sign'
data = {
    'url': "/toutiao/c/user/article/?page_type=1&user_id=50502346173&max_behot_time=0&count=20"
}

res = requests.post(url=url, data=data)
print(res.text)
headers = {
    'accept': 'application/json, text/javascript',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'tt_webid=6809944566961014279; SLARDAR_WEB_ID=98bc5a11-b1cf-4a9b-ad9a-4f77d6dedc9b; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6809944566961014279; csrftoken=4bed4674527d2414c0fb323388bcbfaf; ttcid=a749797515404efbb2a87f38d0b3549779; s_v_web_id=verify_k8gn7oy3_uXveAqKm_RflR_43dG_9K9c_mI0XsKhFMAhm; tt_scid=hw4qwqqr0cU9fVdS8x2ITnOXAC.RKDtKP4PyDAqesR-GpLIMDycqfvozFZL1kqrzd05a',
    'referer': 'https://www.toutiao.com/c/user/50502346173/',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
toutiao_res = requests.get(url=res.text, headers=headers)
print(toutiao_res.text)
print(toutiao_res.status_code)
print(toutiao_res.url)


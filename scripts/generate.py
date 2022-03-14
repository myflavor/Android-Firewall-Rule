import json
import os

github_repo = "https://github.com/zhaobozhen/LibChecker-Rules"

# 调试模式
debug = False
# 关键词
keywords = ["推送", "收集", "广告", "变现", "分析", "热更新", "统计", "上报", "数据采集"]
# 跳过包名
skip_packages = ["com.xiaomi"]
# 筛选组件
components = ["activities", "receivers", "services"]
rule = ""
for component in components:
    path = "LibChecker-Rules/"+component + "-libs/"
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(path + file):
            with open(path + file, encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    name = data['label']
                    description = data['description']
                    package = file.removesuffix(".json")
                    skip = False
                    for skip_package in skip_packages:
                        if skip_package in package:
                            skip = True
                            break
                    if not skip:
                        for keyword in keywords:
                            if keyword in name or keyword in description:
                                rule = rule + package + ",\n"
                                if debug:
                                    print(package, "|", name, "|", keyword)
                                break
                except:
                    print(end="")
with open("rule.txt", 'w') as f:
    f.write(rule)
    f.close()

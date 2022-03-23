# Android-Firewall-Rule
应用净化APP云端规则仓库

Github Action 每天0点同步LibChecker规则并生成通用规则

  rule.txt(云端规则)
  
  exclude_rule.txt(云端排除规则)
  
  manual_rule.txt(手动填写规则)
  

scripts下的generate.py通过libchcker的数据加上描述关键词的筛选生成规则写入到rule.txt

是手动填写的规则，最后会合进rule.txt


LibChecker-Rules.json是克隆LibChecker仓库生成的json，提供APP筛选过滤

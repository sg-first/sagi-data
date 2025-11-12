sagi data
===========

* ndjson是aegis上直接下载下来的原始数据
* `aegisLogFilter.py`中的`filterFrom`负责从ndjson中过滤出特定服务器上的结算数据（主要目的是过滤掉测试服数据）
* `aegisLogFilter.py`中的`getUidHistory`负责从ndjson中筛选指定玩家的所有上报数据
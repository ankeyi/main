urnalctl [-k查看内核日志] [-b 查看系统本次启动的日志] [-u 查看指定服务的日志] -f [追踪日志] -n [指定日志条数]  --since="2022-5-6 15:33:00" 显示该日期之前的所有日志  --until=显示该日期之后的日志
#"显示2017年10月30号，18点10分30秒到当前时间之间的所有日志信息"
journalctl --since="2017-10-30 18:10:30"

#获取昨天的日志如下：
journalctl –since yesterday

#获取某一个时间段到当前时间的前一个小时的日志
journalctl --since 09:00 --until "1 hour ago" 

#获取当前时间的前20分钟的日志
journalctl --since "20 min ago"

#获取某一天到某一个时间段的日志信息
journalctl --since "2017-01-10" --until "2017-01-11 03:00" 

#获取15：15到现在的日志
journalctl --since"15:15" --until now


# 添加kali源


wget archive.kali.org/archive-key.asc //下载签名

apt-key add archive-key.asc //安装签名


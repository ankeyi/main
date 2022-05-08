# 渗透测试阶段

## 情报搜集
google hacking  
社交网络  
目标系统踩点

## 危险建模
使用情报搜集阶段所获得到的信息，来标识出目标系统上可能存在的漏洞和弱点  
危险建模可以确定出最高效的攻击方法，需要进一步获取得到的信息，以及从哪里攻破目标系统

## 漏洞分析
考虑如何获取，目标系统访问权限，分析和理解哪些攻击途径可行，特别需要重点分析端口和漏洞扫描结果

## 渗透攻击
进行大量漫无目的的渗透尝试之后期待奇迹般出现一个shell是痴心妄想，只会造成大量喧嚣的警报，最好是基本确信特定攻击会成功的基础上才真正对目标系统实施渗透攻击

## 报够阶段
编写和报告发现时需要站在客户组织的角度上，来提升安全意识，修补发现的问题

# 术语
## 渗透攻击(Exploit)
Exploit指攻击者利用一个系统、应用或服务中的安全漏洞，所进行的攻击行为

## 攻击荷载(Payload)
Payload是期望目标系统在被渗透攻击之后去执行的代码

## shellcode
shellcode在渗透攻击荷载运行的一组机器指令，shellcode通常以汇编语句编写

## 模块(Module)
模块指Metasploit框架中所使用的一段软件代码组件

## 监听器(Listener)
监听器是Metasoloit中用来等待连入的网络组件，监听器是在攻击主机上等待被渗透攻击的系统来连接，并负责处理这些网络接口

## MSF命令行
                msfconsole -x "use module; set RHOST ip; set PAYLOAD; run"
                msfconsole -r /home/scripts/reverse_tcp.rc

## MSF攻击荷载生成器
                msfvenom -h
## MSF编码器
                列出可用的编码器
                msfvenom -l encoders 

## Nasm shell汇编操作码
                /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb

# 实践
## 情报收集
### 域名查询解析
        whois domain
        dig @<DNS server> <hostname>
                dig -x ip 反查域名
        searchdns.netcraft.com
### google hacking
        intext:  
        intitle:
        cache: url #搜索特定页面的缓存快照
        define: key word #搜索关键字定义来源链接
        filetype:xls xlsx xlt xlsm doc
        site:url #限定搜索范围到特定网站
        related:url #搜索与该url相关的页面
        numrange:1-10 #搜索数字

## 主动扫描
## nmap TCP空闲扫描
        search ipidseq
        use 
        set RHOSTS ip
        set THREADS 1-128
        run
        if(ip==Incrementall)
        nmap -Pn -sS -sI ip ip ip


### Nmap输入结果导入Metasploit数据库
        nmap -sS -O ip -oX host.xml
        db_import host.xml



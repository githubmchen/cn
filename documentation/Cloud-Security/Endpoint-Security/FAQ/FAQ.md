# 常见问题

**Q1：主机安全目前支持什么系统和版本号？**

A1：京东云官方镜像全版本都支持，系统会自动加载主机安全防护功能。

**Q2：主机安全是免费使用吗？**

A2:主机安全基础版是免费提供，主机安全企业版是收费版本。

**Q3：主机安全需要部署安装吗?**

A3：主机安全agent是内置到京东云官方系统镜像中，直接选择官方镜像即可自动加载主机安全功能；对于已有云主机用户需从官方网站下载安装包，进行单独部署。

**Q4：主机安全客户端会收集用户信息吗？客户端会上传什么数据到服务器？**

A4：主机安全客户端不会收集用户信息，只会将客户端生成的安全告警日志上传到服务器。

**Q5：客户端与服务端的数据传输方式是如何的？会导致数据泄露吗？**

A5：客户端采用的是SSL 加密的传输方式将数据传输至服务端，这种加密协议的安全性非常高，不会导致数据泄露。

**Q6：暴力破解具体是如何识别的？Windows 和Linux 都是如何防护的？**

A6：针对RDP 和SSH 的暴力破解是通过日志解析进行识别的，而针对FTP 、MySQL 的暴力破解则是通过网络报文解析进行识别。

**Q7. 暴力破解是如何进行防御封禁的？攻击IP 的封禁时间默认是多久？**

A7. 防暴力破解功能，在Windows 系统下基于网络驱动程序在内核层实现IP 的封禁；而Linux 系统下则是通过维护IPtable 来进行IP 封禁。两种系统防护策略相同，10分钟内爆破5次后IP被封禁，系统默认的封禁时间均为10 分钟。

**Q8. 异地登录时，没有产生告警提醒?**

A8. 需要在控制台界面配置常用登录地。

**Q9. 系统漏洞修复支持什么版本**

A9.系统漏洞修复仅支持Windows系统，Linux系统提供漏洞修复建议需手动完成修复。

**Q10. 系统漏洞检查规则，系统性能会影响很大吗？**

A10.系统漏洞检测时间为凌晨0-5点避开业务高峰期，每天只检测和更新一次，不会影响正常业务使用。

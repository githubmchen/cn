## FAQ

**Q：jdcloud-codedeploy.yml中的hooks是否支持执行命令？**

A：支持，hooks需要填写的command项为脚本所在的位置或执行脚本的命令本身。

**Q：如何处理上一次部署任务的缓存呢？**

A：若本次部署成功，那么上次部署任务的缓存将成为备份；若本次部署失败，那么本次缓存将被删除。

**Q：Agent的端口是什么？**

A：agent采用的是2001和2002端口，如果云主机采用了安全组，请将安全组的出站规则2001和2002端口打开。

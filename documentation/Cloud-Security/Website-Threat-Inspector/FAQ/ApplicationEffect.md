# 业务影响问题

### 1、扫描是否影响网站业务？

- 根据业务类型不同，合理设置扫描速度，不会影响网站业务

### 2、为什么搭建了靶场，但是未扫描出漏洞？

 - 查看安全组是否开放了扫描器Worker的访问权限
 - 如果是web类别靶场且需要登录进行验证的漏洞， 请确认cookie设置是否正确
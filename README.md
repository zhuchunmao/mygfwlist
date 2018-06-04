# mygfwlist
本项目中包括2个文件<br>
1、国外常见被屏蔽的IP地址<br>
2、生成openvpn的 route *** *** vpn_gateway  脚本<br>
3、脚本是通过python 编写的，如果想使用脚本请安装如下环境<br>
以Centos举例<br>
yum install python python-pip<br>
pip install netaddr<br>
5、使用方法<br>
cd /root/<br>
wget https://raw.githubusercontent.com/zhuchunmao/mygfwlist/master/ovpn_router.py<br>
chmod +x /root/ovpn_router.py<br>
/root/ovpn_router.py<br>
最终会生成一个文件/root/router

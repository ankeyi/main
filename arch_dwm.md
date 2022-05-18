
# archlinux system install
前面和wiki走就ok
systemctl stop reflector
pacstrap /mnt base linux linux-headers linux-firmware
进去 /mnt 后用  arch-chroot /mnt
 ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
vim /etc/locale.gen   去掉 en_US.UTF-8 and zh_CN.UTF-8 的注释
locale=gen
echo "an" > /etc/hostname
echo "127.0.0.1         localhost" > /etc/hosts
sudo pacman -S amd-ucode sudo
passwd
useradd -m an
passwd an
pacman -S grub  efibootmgr

grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
pacman -S w3m xorg plasma-desktop w3m xcompmgr wqy-zenhei  networkmanager network-manager-applet networkmanager-pptp libx11 libxft libxinerama base-devel
systemctl enable NetworkManager
vim /etc/sudoers        add an
su an
w3m st.suckless.org
tar zxvf st*
cd st*
make
sudo make clean install
kde切换成中文然后开机自启动(设置里)脚本
pacman -S   polphin  #文件管理


# enable default network 
	virsh net-autostart default 
# start default network 
	virsh net-start default

# kali源签名
wget archive.kali.org/archive-key.asc //下载签名

apt-key add archive-key.asc //安装签名
# connect network 手动连接配置网络
	vim /etc/network/in*
*	allow-hotplug wlp1s0
*	iface wlp1s0 inet dhcp
*	wpa-ssid wifi_name
*	wpa-psk	 password


# 安装编译dwm dmenu st 所需环境
### debian linux system
	sudo apt install  feh ttf-wqy-zenhei w3m vim xorg git build-essential libx11-dev libxft-dev libxinerama-dev xcompmgr surf fcitx5 fcitx5-rime

### arch linux system
	sudo apt install wqy-zenhei w3m vim xorg git build-essential libx11 libxft libxinerama xcompmgr  fcitx5 fcitx5-rime


# 亮度  需要root权限
	echo num > /sys/class/backlight/amdgpu_bl0/brightness


## dwm 启动前提---配置好.xinitrc  
### 壁纸管理 feh 打开桌面随机使用背景 
	feh --bg-max --randomize ~/.img/*  &
### 透明终端
	xcompmer &
### 执行命令
	fcitx5 &
	xcompmgr &
### 状态栏显示电量和时间
while true; do
        batt=$(LC_ALL=C acpi -b)

        case $batt in
        *Discharging*)
                batt="${batt#* * * }"
                batt="${batt%%, *} "
                ;;
        *)
                batt=""
                ;;
        esac

        xsetroot -name "$batt$(date +%R)"

        sleep 60
done &

	exec dwm

# 快捷键
	Mod1+p start Dmenu
	Shift+Mod1+x 将当前活动窗口移动到x(序号)标签
	Shift+Mod1+C 关闭当前活动窗口
	Mod1+F	     浮动模式
	Mod1+M	     单页模式
	Mod1+T	     平铺模式
	Shift+Mod1+Q 退出DWM

# vim不能使用输入法
	open fcitx5 wiki



# 调整声音先开启这个
 sudo pacman -S alsa-utils
alsamixer
# 如果是kde
 	vim ~/.asoundrc 
defaults.pcm.card 1
defaults.pcm.device 0
defaults.ctl.card 1
就好量

# Connect WIFI
	sudo pacman -S dhcpcd iwd
	sudo systemctl enable iwd

# connect pptp
	sudo pacman -S pptpclient
	sudo pptpsetup --create xinjiapo --server likeni.org --username  user --password pass --encrypt
# route  pacman -S net-tools
ip route add default dev ppp0

# 截屏
	sudo pacman -S imagemagick
	import -window root img_name

# 调整分辨率
	xrandr
	xrandr -s  分辨率

# install ruby jekyll
	sudo pacman -S ruby ruby-docs rubygems
	gem install jekyll bundler --user-instal
	export PATH="/home/an/.local/share/gem/ruby/3.0.0/bin:$PATH"
	jekyll -v
	bundle add webrick
	jekyll new myblog
	cd myblog
	bundle exec jekyll serve

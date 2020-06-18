red='\033[1;31m'
white='\033[1;37m'
green='\033[1;32m'

printf "$red"
echo "INSTALLATION STARTED WAIT BUDDY :)" | pv -qL 10
pkg install -y pv ruby  git curl php python python2 wget termux-api zip
gem install colorize
pip install lolcat
pip2 install beautifulsoup4
pip2 install termcolor
pip2 install argparse
pip2 install request
pip2 install pysocks
pkg install mpv
pkg install libcurl
printf "$green"
echo "You Need to install Termux API APP For some
commands" | pv -qL 10
printf "$green"
echo "Please install Termux API from
playstore" | pv -qL 10
termux-open-url https://play.google.com/store/apps/details?id=com.termux.api
printf "$red"
echo "INSTALLATION FINISHED :)
U CAN STRAT TOOL BY python2 mutool.py :]" | pv -qL 10

fi

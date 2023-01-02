#! /bin/sh

### BEGIN INIT INFO
# Provides: listen-for-cast.py
# Required-Start: $remote_fs $syslog
# Required-Stop: $remote_fs $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
### END INIT INFO

# If you want a command to always run, put it here Carry out specific functions when asked

# to by the system
case "$1" in
	start)
		echo "Starting listen-for-cast.py"
		/etc/auxcast/listen-for-cast.py &
		;;
	stop)
		echo "Stopping listen-for-cast.py" pkill -f
		/etc/auxcast/listen-for-cast.py
		;;
	*)
		echo "Usage: /etc/init.d/listen-for-cast.sh {start|stop}" exit 1
		;;
esac

exit 0

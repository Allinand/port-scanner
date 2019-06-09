import socket
import sys

timeout = .12

def usage_prompt():
	print "Usage:\n\tpython scan_p.py [HOST_OPT] [ENUM_OPT]"
	print "\nNOTE: One attempt made per socket, no retry\n"
	print "\n[HOST_OPTS]"
	print "\t-h\t\tHost to be scanned"
	print "\t-p\t\tSpecify port for enumeration"
	print "\t-v\t\tVerbose output (lists all fails)"
	print "\n[ENUM_OPTS]"

def hostUp(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(timeout)
	try:
		s.connect((host, port))
		s.shutdown(socket.SHUT_RDWR)
		return True
	except:
		return False
	finally:
		s.close()

def scan_p(host, port, verbose):
	print "[HOST] {}".format(host)
	# Open port scan
	open_ports = []
	if port == 0:
		for test_port in range(1, 65536):
			if hostUp(host, test_port):
				print "[RECV]\t\t{}".format(test_port)
				open_ports.append(port)
			else:
				if verbose:
					print "[FAIL]\t\t{}".format(test_port)

		print "\n[COMPLETE]\nOpen Ports:"
		for test_port in open_ports:
			print "{}\t\t".format(test_port)

	# Enumeration or single-port test
	else:
		if hostUp(host, port):
			print "[RECV]\t\t{}:{}".format(host, port)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		usage_prompt()
	else:
		host = ""
		port = 0
		verbose = False
		for index in range(1, len(sys.argv)):
			if sys.argv[index][0] == "-":
				if sys.argv[index][1] == "h":
					host = sys.argv[index + 1]
				elif sys.argv[index][1] == "p":
					port = int(sys.argv[index + 1])
				elif sys.argv[index][1] == "v":
					verbose = True
				else:
					print "[ERR]\t\tInvalid syntax"
					usage_prompt()
				#elif len(sys.argv[index]) > 2:
				#	args = multi_args(sys.argv[index])
				#elif enum opts
		if host == "":
			usage_prompt()
		else:
			scan_p(host, port, verbose)

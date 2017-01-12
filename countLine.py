from queue import Queue
import os


def isValidFile(f):
	validSuffix = [".cpp", ".c", ".h", ".py", ".sh", ".java",]
	return os.path.isfile(f) and os.path.splitext(f)[1] in validSuffix


def countLine(p = "."):
	res = 0
	q = Queue()
	q.put(p)
	while not q.empty():
		curDir = q.get()
		fls = os.listdir(curDir)
		for f in fls:
			f = os.path.join(curDir, f)
			if os.path.isdir(f):
				q.put(f)
			elif isValidFile(f):
				with open(f, "r") as fl:
					try:
						res = res + len(fl.readlines())
					except UnicodeDecodeError as e:
						print("cannot read %s because %s" % (f, e))
	return res


if __name__ == "__main__":
	print(countLine())

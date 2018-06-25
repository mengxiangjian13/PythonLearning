import subprocess

sub = subprocess.Popen(['open','douban.txt'])
a = sub.wait()
b = sub.poll()
print(str(a),str(b))

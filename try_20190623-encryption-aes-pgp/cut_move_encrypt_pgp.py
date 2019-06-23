import shutil
import os
import sched, time
import gnupg

s = sched.scheduler(time.time, time.sleep)
gpg = gnupg.GPG(gpgbinary="C:\\path...\\gpg.exe")
input_data = gpg.gen_key_input(
    name_email='me@email.com',
    passphrase='password',
)
key = gpg.gen_key(input_data)
print(key)
ascii_armored_public_keys = gpg.export_keys(key.fingerprint)
ascii_armored_private_keys = gpg.export_keys(
    keyids=key.fingerprint,
    secret=True,
    passphrase='passphrase',
)

# export
with open('mykeyfile.asc', 'w') as f:
    f.write(ascii_armored_public_keys)
    f.write(ascii_armored_private_keys)

# import
with open('mykeyfile.asc') as f:
    key_data = f.read()
import_result = gpg.import_keys(key_data)

for k in import_result.results:
    print(k)

def move2folder(sc):

    source = 'C:\\path'
    dest1 = 'C:\\path2'

    files = os.listdir(source)

    for f in files:

            status = gpg.encrypt_file(
                file=f,
                recipients=['me@email.com'],
                output='encrypted.txt.gpg',
            )

            shutil.move(source + f, dest1)

    s.enter(5, 1, move2folder, (sc,))

s.enter(5, 1, move2folder, (s,))
s.run()


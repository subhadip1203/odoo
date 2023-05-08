### get odoo
git clone --branch 15.0 --depth=1 https://github.com/odoo/odoo.git

### enable Running Scripts
open powerShell as admin

run `get-executionpolicy` :this will show restricted

run `set-executionpolicy remotesigned`



### virtual env ubuntu WSL

install virtual env in laptop : `sudo apt install python3-venv`

install vEnv in the project : `sudo python3 -m venv myenv`

activate vEnv : `source myenv/bin/activate`


### ubuntu extra installation:

first try:
`sudo apt-get -y install python3-psycopg2 python3-dev libpq-dev libsasl2-dev libldap2-dev libssl-dev`

second try : (if python version is 3.10 , then put python3.10-dev)
`sudo apt-get install build-essential libpcap-dev libssl-dev libffi-dev python3.10-dev `

third try : 
`sudo apt-get install --reinstall  libavdevice-dev libavfilter-dev libopus-dev libvpx-dev pkg-config libsrtp2-dev`



### install packages
`pip install wheel`

`pip install -r requirements.txt`

`pip install pyopenssl==22.1.0`


### install wkhtmltopdf in ubuntu

wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

tar vxf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz 

cp wkhtmltox/bin/wk* /usr/local/bin/

### create conf

create folder named : conf

create file : odoo.conf

inside that put details:

    admin_passwd = admin123
    db_host = localhost
    db_port = 5432
    db_user = odoo
    db_password = 12345
    db_maxconn=40
    addons_path = /mnt/c/Users/zz-spahari/Desktop/subhadip/odoo/project/odoo/addons
    http_port=8015

*** special note : as I am using WSL-Ubuntu , so my path is /mnt/.....


### run odoo
source myenv/bin/activate

python3  ./odoo-bin -c conf/odoo.conf


### run unit test

python3  ./odoo-bin -c conf/odoo.conf --test-tags /fleet
python3  ./odoo-bin -c conf/odoo.conf --test-tags /om_hospital


### user details

user name: subhadipsjsc@gmail.com
password : admin123




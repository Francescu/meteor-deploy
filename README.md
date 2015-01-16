# meteor-deploy
## Todo
- Script which configure all of this
- Actual explanations
- Link sources

## simple nginx conf file
`/etc/nginx/sites-enabled/myproject.conf`

1. change settings in file (site URL)
2. note that here PORT used is 3001
3. link the file to sites-available with `ln -s`

TODO/WIP:
- Add required installations (`apt-get install nginx` etc.)
- Put SSL config
- Apache2 too?

## debian conf file for init.d (sysvinit)
`/etc/init.d/myproject`

1. Rename to project name `mv /etc/init.d/myproject /etc/init.d/NAME`
2. `chmod +x /etc/init.d/NAME`
3. change settings inside (be careful mongodb name is the same as the filename, PORT is 3001)
4. You can now use `sudo service NAME start` (or stop, restart and status)

TODO/WIP:
- Explain more how to edit the file (create a little generator?)
- Add node & dependencies installations
- Find out when to use `meteor bundle` + `node main.js` like here, use directly `meteor`, or use future
- Put others init.d configs like *upstart* (supervisor too?) 
- ?write configs for `meteor` and `future` deployments?

## auto deployment from git
`/home/user/myproject/fabfile.py`

1. Change file to edit `project_name`
2. Put your git repo in src `cd /home/user/myproject/; git clone <REPO>; mv <REPONAME> src` 
3. use `fab update` (require `pip install fabric`)

TODO/WIP
- Explicit dependencies `python`, `pip`, `fabric` etc.
- Make more options for deployment (like path etc.)
- Find out how to perform hot deployments?
- Explain default structure and commands
- makefile / rakefile too? 

## links / sources
- https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps
- https://github.com/fhd/init-script-template/blob/master/template

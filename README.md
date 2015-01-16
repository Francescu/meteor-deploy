# meteor-deploy-nginx
## Todo
- Script which configure all of this
- Actual explanations
- Link sources

## simple nginx conf file
`/etc/nginx/sites-enabled/myproject.conf`
> reminders:
> change settings inside (site URL)
> PORT used is 3001
> link it to sites-available with `ln -s`

TODO..

## debian conf file for init.d (sysvinit)
`/etc/init.d/project`

> reminders:
> set `chmod +x /etc/init.d/project`
> change settings inside (be careful mongodb name is the same as the filename)

TODO..

## auto deployment from git
`/home/user/project/fabfile.py`

> reminders:

todo explain default structure

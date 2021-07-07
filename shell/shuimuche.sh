#! /bin/bash
SHUIMUCHE="/home/wwwroot/shuimucar-web"
SHUIMUCHE_BACK="/home/wwwroot/shuimucar-web".`date +%Y%m%d`
WORK="/home/wwwroot"

function backup_dict() {
    echo "开始备份项目目录。。。"
    cp -r $SHUIMUCHE $SHUIMUCHE_BACK
    echo "备份完成。。。"
}


function update() {
    echo "更新项目。。。"
    cd $SHUIMUCHE
    git fetch --all
    git reset --hard origin/master
    git pull origin master
}

function delete_dict() {
    find /home/wwwroot/ -mtime +30 -name "shuimucar-web.*" -delete
}

function change_chmod() {
    echo "修改目录权限。。。"
    chmod 777 /home/wwwroot/shuimucar-web/cache
    chmod 777 /home/wwwroot/shuimucar-web/templates_c
    chmod 777 /home/wwwroot/shuimucar-web/upload
}

backup_dict
update
delete_dict
change_chmod

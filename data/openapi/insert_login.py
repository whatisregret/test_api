import random
from utils.other_utils.fakerutils import get_phone, get_email, get_male_name
from utils.mysql_utils.mysql_utils import execute, query
from utils.other_utils.time_utils import now_time_second


def insert_login():
    id_c = "zxc" + str(random.randint(100, 1000))
    phone = get_phone()
    email = get_email()
    name = get_male_name()
    sql_oauth = "INSERT INTO `oauth-center`.oauth_client_details (client_id,client_secret,client_secret_str,scope,authorized_grant_types,access_token_validity,refresh_token_validity,additional_information,autoapprove,create_time,update_time,client_name,support_id_token,id_token_validity) VALUES('" + id_c \
                + "','{bcrypt}$2a$10$y8W1eee88LEKiAzxyOIssOTKYsfl6bIPF70amz9WMtCZpDy1gf1VG','" + id_c + "','all','authorization_code,password,client_credentials,implicit,refresh_token,password_code,openId,mobile_password,email_password',18000,28800,'{}','true','" \
                + str(now_time_second()) + "','" + str(now_time_second()) + "','" + id_c + "',1,60)"
    execute(sql_oauth)
    sql_ser = "INSERT INTO `user-center`.`sys_user` VALUES (null,'" + name + "', '{bcrypt}$2a$10$s/5HsFD9iDIUZPsVmZxUVuYlBPXreDh/c41ASv1DVgUixNFqLre0y', 'test101', '1010', '" + phone + "', 1, 1, 'ORG', '" + str(
        now_time_second()) + "', '" + str(now_time_second()) + "', NULL, NULL, 0, '" + email + "');"
    execute(sql_ser)
    sql_select_info = "select MAX(enterprise_no) from `manager-center`.enterprise_info "
    enterprise = str(int(query(sql_select_info, state="1")["MAX(enterprise_no)"]) + 1)
    sql_info = "INSERT INTO `manager-center`.enterprise_info VALUES (null, '" + enterprise + "', '深圳市" + name + "设计有限公司', '前海', '" + phone + "', '" + email + "', 'webAPP', 0, '" + str(
        now_time_second()) + "', '" + str(now_time_second()) + "');"
    execute(sql_info)
    sql_access_key = "select MAX(id) from `oauth-center`.oauth_client_details"
    access_key = query(sql_access_key, state="1")["MAX(id)"]
    sql_account = "INSERT INTO `tenant_account` VALUES (null, '" + id_c + "', " + str(
        access_key) + ", 'webApp', '" + name + "', '" + name + "', '" + str(phone) + "', '" + email + "', 0, '" + str(
        now_time_second()) + "', '" + str(now_time_second()) + "', '" + str(now_time_second()) + "');"
    execute(sql_account)
    print(email)


if __name__ == '__main__':
    insert_login()

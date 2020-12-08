---
layout: post
title: Утстановка Oracle DB Docker Mac
comments: False
category: [sql] [mac]
tags: [sql] [mac]
---

Лучше не читать все что снизу

[Install Oracle database on Docker and connect with SQL Developer](https://www.youtube.com/watch?v=ciYsDbBx80s&ab_channel=ShowMeYourCode%21)

1. Log into Docker hub (in order to access oracle repository)
```docker login```

2. Download image
```docker pull store/oracle/database-enterprise:12.2.0.1```

3. Run image
```docker run -d -p 1521:1521 --name oracle store/oracle/database-enterprise:12.2.0.1```
4. Connect to container
```docker exec -it oracle bash -c "source /home/oracle/.bashrc; sqlplus /nolog"```

5. Copy below script to open SQL shell

```connect sys as sysdba;```
 -- Here enter the password as 'Oradoc_db1'

```sql 
alter session set "_ORACLE_SCRIPT"=true;
create user dummy identified by dummy;
GRANT ALL PRIVILEGES TO dummy;
```

4. Configure SQL Developer

- Username: dummy
- Password: dummy
- Hostname: localhost
- Port: 1521
- Service name: ORCLCDB.localdomain

Вин




Источники:
- [Oracle Database Enterprise Edition](https://hub.docker.com/_/oracle-database-enterprise-edition)
- [Setting up Oracle Database on Docker](https://oralytics.com/2017/04/21/setting-up-oracle-database-on-docker/)
- [Oracle DataBase – ERROR: ORA-12162: TNS:net service name is incorrectly specified](https://sanaebekkar.wordpress.com/2016/03/17/oracle-database-error-ora-12162-tnsnet-service-name-is-incorrectly-specified/)
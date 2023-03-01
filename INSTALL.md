1. install postgres server
2. fill DB_* info out in .env (reference at .env.template)
3. run db_init.sql on the postgres server
4. install python3/pip with your package manager
5. ``pip install -r requirements.txt``
6. add ``https://discord.com/oauth2/authorize?client_id=1078941290781212723&permissions=8&scope=applications.commands+bot`` to server
7. ``python3 run.py``
BEGIN TRANSACTION;
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES ('58b010n47k3lsdhhikhv9w6jelx290vo','Y2ZiNDhhZDM4YzJjZTA1MDFjMjUxOWUxZDkxYzBjMDI2NjY1YjY2YTp7Il9hdXRoX3VzZXJfaGFzaCI6IjQwODYwZDUzYzYxODRhNGZiMDNiZTA1ZWUzZDFjOGQ1Yzg1MGUxNjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-08-03 04:01:35.776000');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2015-07-20 04:00:36.558000');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2015-07-20 04:00:36.607000');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2015-07-20 04:00:36.653000');
INSERT INTO "django_migrations" VALUES (4,'bid','0001_initial','2015-07-20 04:00:36.736000');
INSERT INTO "django_migrations" VALUES (5,'sessions','0001_initial','2015-07-20 04:00:36.759000');
INSERT INTO "django_migrations" VALUES (6,'bid','0002_auto_20150720_1203','2015-07-20 04:03:44.518000');
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL, UNIQUE ("app_label", "model"));
INSERT INTO "django_content_type" VALUES (1,'log entry','admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES (3,'group','auth','group');
INSERT INTO "django_content_type" VALUES (4,'user','auth','user');
INSERT INTO "django_content_type" VALUES (5,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'session','sessions','session');
INSERT INTO "django_content_type" VALUES (7,'product','bid','product');
INSERT INTO "django_content_type" VALUES (8,'work sheet','bid','worksheet');
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
INSERT INTO "django_admin_log" VALUES (1,'2015-07-20 05:39:40.501000','1','Product object',2,'Changed name, price, website and description.',7,1);
CREATE TABLE "bid_worksheet" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(150) NOT NULL, "file" varchar(100) NOT NULL, "pub_date" datetime NOT NULL, "pdf" varchar(100) NOT NULL, "creator_id" integer NULL REFERENCES "auth_user" ("id"));
CREATE TABLE "bid_product" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "bid_price" decimal NOT NULL, "name" varchar(30) NOT NULL, "publish_date" date NOT NULL, "price" decimal NOT NULL, "expire_date" date NOT NULL, "photo" varchar(100) NOT NULL, "website" varchar(500) NOT NULL, "description" text NOT NULL);
INSERT INTO "bid_product" VALUES (1,600,'Iphone 6','2015-07-20',500,'2015-07-27','./apple-iphone-6-16gb-silver-2338-819948-1-zoom_YAu6PKO.jpg','http://www.lazada.com.my/refurbished-apple-iphone-6-128gb-gold-1778467.html','<ul class="prd-attributesList ui-listBulleted">
<li><span>8MP Main Camera</span></li>
<li><span>1.2MP Front Camera</span></li>
<li><span>4.7-inch LED-backlit IPS LCD</span></li>
<li><span>GPRS / EDGE / Wi-Fi / Bluetooth v4.0</span></li>
<li><span>Non-removable Li-Po 1810 mAh battery</span></li>
<li><span>128GB Capacity</span></li>
<li><span>1 GB RAM</span></li>
<li><span>1-Year insurance&nbsp;protection for cracked screen&nbsp;</span></li>
</ul>');
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("user_id", "permission_id"));
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), UNIQUE ("user_id", "group_id"));
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NOT NULL, "is_superuser" bool NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL);
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$15000$sK19t8VV2HlI$pQLb/QcJrt3MnO86XOAOOuPViVE+u8XUM/RCWiDZ9lE=','2015-07-20 04:01:35.763000',1,'admin','','','',1,1,'2015-07-20 04:01:10.696000');
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, UNIQUE ("content_type_id", "codename"));
INSERT INTO "auth_permission" VALUES (1,'Can add log entry',1,'add_logentry');
INSERT INTO "auth_permission" VALUES (2,'Can change log entry',1,'change_logentry');
INSERT INTO "auth_permission" VALUES (3,'Can delete log entry',1,'delete_logentry');
INSERT INTO "auth_permission" VALUES (4,'Can add permission',2,'add_permission');
INSERT INTO "auth_permission" VALUES (5,'Can change permission',2,'change_permission');
INSERT INTO "auth_permission" VALUES (6,'Can delete permission',2,'delete_permission');
INSERT INTO "auth_permission" VALUES (7,'Can add group',3,'add_group');
INSERT INTO "auth_permission" VALUES (8,'Can change group',3,'change_group');
INSERT INTO "auth_permission" VALUES (9,'Can delete group',3,'delete_group');
INSERT INTO "auth_permission" VALUES (10,'Can add user',4,'add_user');
INSERT INTO "auth_permission" VALUES (11,'Can change user',4,'change_user');
INSERT INTO "auth_permission" VALUES (12,'Can delete user',4,'delete_user');
INSERT INTO "auth_permission" VALUES (13,'Can add content type',5,'add_contenttype');
INSERT INTO "auth_permission" VALUES (14,'Can change content type',5,'change_contenttype');
INSERT INTO "auth_permission" VALUES (15,'Can delete content type',5,'delete_contenttype');
INSERT INTO "auth_permission" VALUES (16,'Can add session',6,'add_session');
INSERT INTO "auth_permission" VALUES (17,'Can change session',6,'change_session');
INSERT INTO "auth_permission" VALUES (18,'Can delete session',6,'delete_session');
INSERT INTO "auth_permission" VALUES (19,'Can add product',7,'add_product');
INSERT INTO "auth_permission" VALUES (20,'Can change product',7,'change_product');
INSERT INTO "auth_permission" VALUES (21,'Can delete product',7,'delete_product');
INSERT INTO "auth_permission" VALUES (22,'Can add work sheet',8,'add_worksheet');
INSERT INTO "auth_permission" VALUES (23,'Can change work sheet',8,'change_worksheet');
INSERT INTO "auth_permission" VALUES (24,'Can delete work sheet',8,'delete_worksheet');
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("group_id", "permission_id"));
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE INDEX "bid_worksheet_3700153c" ON "bid_worksheet" ("creator_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
COMMIT;

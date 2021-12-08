#  Thingsboard Custom Front End Builder
Simple tool to help repack thingsboard.jar dependencies files (BOOT-INF/lib).

**Built mainly to update ui-ngx.jar file with a modified version, but basically you could update any files you want that goes belong to BOOT-INF/lib directory, just put in on put_ui-ngx_here folder.**

**Tested for Thingsboard v3.1.1.**

Built on Python3.

**To run this program :**
 - **Terminal**
	 -  Open terminal from this script directory, and execute **python3 ThingsboardCustomBuilder.py**

**Prerequisite** : **nothing?**

**Known Bugs :**
- After repacking **thingsboard.jar**, if you try to put it back to **/usr/share/thingsboard/bin** folder and replace the **unmodified** thingsboard.jar, you won't be able to start thingsboard service via **service thingsboard start**.
- Therefore, with this tools, your working **thingsboard.yml** file will be embedded to **generated** **thingsboard.jar** **of your modified version**. So you can still start your service manually by executing **java -jar thingsboard.ja**r on your **modified thingsboard.jar version**, and your thingsboard service should start like normal.
- In future build, I'm gonna try to make a custom service to replace unworking service as I've explained before.

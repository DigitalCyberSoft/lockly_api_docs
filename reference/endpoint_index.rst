REST endpoint index
====================

Every REST endpoint observed in the Lockly Android apps' Retrofit interfaces
(``ApiService`` and ``PGNetManager``), grouped by area. The base URL is
``https://apiserv03c.lockly.com/pgsmtlkv2/api/`` and every endpoint is a
``POST`` unless noted (``backup/ekeyOrEbadge``, ``channel`` and the ``iap/get*``
reads are ``GET``). This is an index only — request/response bodies and the
RSA/DES3 encryption that wraps them are described on the detailed endpoint pages
and in :doc:`/rest/api_format` and :doc:`/rest/encryption`.

Purposes are read from method names and logging strings in the decompiled apps
(🔎 code-traced); treat them as a guide, not a contract. Endpoints marked
"(Manager app)" appear only in Lockly Manager (``com.lockly.smartlock.pro``),
the installer/property app. The ``authSpace/`` prefix is the Lockly Access
Portal (LAP) workspace variant of the correspondingly named consumer endpoint.

.. note::

   341 distinct endpoints are listed (310 in the consumer/Home apps, 31 only in
   Manager). Being listed means the app references the endpoint; it does not
   mean the server still honours it (e.g. the staff endpoints have no callers in
   current consumer builds — see :doc:`/ble/commands/enrolment`).

Account & authentication
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``backac``
     - Back up account
     - 
   * - ``check/token``
     - Validate current token
     - 
   * - ``checkCode``
     - Check a verification code
     - 
   * - ``checkEmailToken``
     - Verify email verification code
     - 
   * - ``checkHaveChildUser``
     - Check for sub-accounts
     - 
   * - ``getUserInfoAndDvList``
     - Lighter account query (locks + key)
     - 
   * - ``getUserWorkSpace``
     - Get user's LAP workspace
     - 
   * - ``image/upload``
     - Upload account profile image
     - 
   * - ``lockly/checkSecureQuestion``
     - Verify security-question answer
     - 
   * - ``lockly/checkVerifCode``
     - Verify a verification code
     - 
   * - ``lockly/getSecurityIssues``
     - List security questions
     - 
   * - ``lockly/logout``
     - Delete account / log out
     - 
   * - ``lockly/renewpwToken``
     - Renew password-change token
     - 
   * - ``lockly/saveSecurityIssue``
     - Save security question answer
     - 
   * - ``lockly/updatePw``
     - Change child-account password
     - 
   * - ``lockly/updatemobile``
     - Update account phone number
     - 
   * - ``online/sendCode``
     - Send a one-time code (login/verify)
     - 
   * - ``priqrymore``
     - Check token still effective
     - 
   * - ``qrylknew``
     - Query account: lock list + DES3 user key
     - 
   * - ``sendEmail``
     - Send email verification code
     - 
   * - ``updac``
     - Change account password
     - 
   * - ``updnm``
     - Update account/user display name
     - 
   * - ``userCheck``
     - Check whether an account exists
     - 

Locks & live commands
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``checkOwnerDvMedium``
     - Check owner credentials on device
     - 
   * - ``chkdid``
     - Check device ID
     - 
   * - ``cp/dvInfo``
     - Get device info (camera/P2P)
     - 
   * - ``cp/dvlist``
     - List devices (camera/P2P)
     - 
   * - ``device/medium/list``
     - List device credentials (Manager app)
     - 
   * - ``device/name/change``
     - Rename lock
     - 
   * - ``device/setting/get``
     - Get device preset
     - 
   * - ``device/setting/getByBleName``
     - Get preset by BLE name
     - 
   * - ``device/setting/getByDeviceId``
     - Get preset by device ID
     - 
   * - ``device/setting/getByP2pId``
     - Get preset by P2P ID
     - 
   * - ``device/setting/getRefTo``
     - Get preset reference
     - 
   * - ``deviceCheck``
     - Check device state/validity
     - 
   * - ``dvKeypadSnBinding``
     - Bind keypad serial to device
     - 
   * - ``forbidenOrStartDevice``
     - Disable or enable a device
     - 
   * - ``get/deviceConfigInfo``
     - Get camera/detection config
     - 
   * - ``getDeviceMc``
     - Get host master code
     - 
   * - ``getDvAdapterFunc``
     - Get lock's supported command set
     - 
   * - ``getDvInfoByKeypadSn2``
     - Get device info by keypad serial
     - 
   * - ``getSysParaList``
     - Get system parameter / reason list
     - 
   * - ``getThirdLockLowVer``
     - Get third-party lock low version
     - 
   * - ``lock/cachedstatus/get``
     - Server-cached lock status (hub fw>=422)
     - 
   * - ``lock/hub/setmc``
     - Set master code via hub
     - 
   * - ``lockly/syspara``
     - OTA / system-parameter info
     - 
   * - ``removeAll/serverLockMedium``
     - Wipe all server-side credential records
     - 
   * - ``rmlkinfo``
     - Delete / remove a lock
     - 
   * - ``update/deviceConfig``
     - Update lock configuration
     - 
   * - ``updateDevice``
     - Update lock metadata
     - 

Hubs, rooms & properties
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``addhub/bindlock``
     - Bind a lock to a hub
     - 
   * - ``addhub/preset``
     - Hub preset setup
     - 
   * - ``addhub/scanlock``
     - Scan for locks via hub
     - 
   * - ``addhub_mq``
     - Add hub (MQTT provisioning)
     - 
   * - ``addroom``
     - Add a room
     - 
   * - ``bindLockAsync``
     - Bind lock asynchronously
     - 
   * - ``deleteprd``
     - Delete property/house
     - 
   * - ``hub/getinfo``
     - Get hub info / MQTT details
     - 
   * - ``hub/updateWakeInd``
     - Update hub wake indicator (wake lock)
     - 
   * - ``hub/updinf``
     - Update hub info
     - 
   * - ``matter/bindHub``
     - Bind a Matter hub
     - 
   * - ``matter/unbindHub``
     - Unbind a Matter hub
     - 
   * - ``saveprd``
     - Create property/house
     - 
   * - ``updateprd``
     - Update property/house
     - 

Credentials & users
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``acu/admin/save``
     - Create admin access user
     - 
   * - ``acu/crdntl/list``
     - List a user's credentials
     - 
   * - ``acu/delete``
     - Delete access user
     - 
   * - ``acu/getUserAcuId``
     - Get a user's ACU id
     - 
   * - ``acu/list``
     - List users
     - 
   * - ``acu/migrate``
     - Transfer/replace admin
     - 
   * - ``acu/multi/auth/save``
     - Save multi-user authentication rule
     - 
   * - ``acu/multi/auth/select``
     - Fetch multi-user authentication rule
     - 
   * - ``acu/name/update``
     - Rename access user
     - 
   * - ``acu/numem/check``
     - Check user name + email
     - 
   * - ``acu/save``
     - Create access user
     - 
   * - ``acu/uid/checkFull``
     - Check whether user slots full
     - 
   * - ``acuid/check``
     - Validate user id
     - 
   * - ``checkPwIsRepeat``
     - Check passcode not reused
     - 
   * - ``crdntl/delete``
     - Delete passcode or sensor
     - 
   * - ``crdntl/ebadge/add``
     - Add eBadge credential
     - 
   * - ``crdntl/face/add``
     - Add face credential
     - 
   * - ``crdntl/fpt/add``
     - Add fingerprint credential
     - 
   * - ``crdntl/list``
     - List credentials
     - 
   * - ``crdntl/pw/add``
     - Add passcode credential
     - 
   * - ``crdntl/pw/update``
     - Update passcode credential
     - 
   * - ``crdntl/pwList/active``
     - Activate passcode on lock
     - 
   * - ``crdntl/pwList/active1``
     - Activate passcode from guest
     - 
   * - ``crdntl/rfid/add``
     - Add RFID card credential
     - 
   * - ``crdntl/sensor/update``
     - Update sensor/credential
     - 
   * - ``crdntl/tapcom/add``
     - Add TapCom credential (Manager app)
     - 
   * - ``du/batchUpdateFpCodes``
     - Batch-update fingerprint codes
     - 
   * - ``du/remove``
     - Remove user name
     - 
   * - ``du/save``
     - Save/back up user name
     - 
   * - ``edit/admDvActiveVal``
     - Activate sub-admin on device
     - 
   * - ``fingerprint/save``
     - Upload fingerprint info
     - 
   * - ``forbidenOrStartUser``
     - Disable or enable a user / sub-account
     - 
   * - ``genomktk``
     - Generate one-time master key token
     - 
   * - ``getDvRfidList``
     - List device RFID cards
     - 
   * - ``getEkeyList``
     - List eKeys/credentials on a lock
     - 
   * - ``getFaceCode``
     - Get face code
     - 
   * - ``getFingerprintList``
     - List fingerprints
     - 
   * - ``getFpCode``
     - Get fingerprint code
     - 
   * - ``getFpCodes``
     - Get fingerprint codes
     - 
   * - ``getRfidCode``
     - Get RFID code
     - 
   * - ``getusedomk``
     - Get used one-time master key
     - 
   * - ``setAndGetCardSysDvConfig``
     - Get/set eBadge card-system config
     - 
   * - ``v2/du/remove``
     - Remove tenant access user
     - 
   * - ``v2/getDvRfidList``
     - List tenant RFID cards
     - 
   * - ``v2/getEkeyList``
     - List tenant eKeys
     - 
   * - ``v2/getFingerprintList``
     - List tenant fingerprints
     - 

Staff & attendance
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``addStaffUser``
     - Add staff user
     - 
   * - ``createStaffLockPw``
     - Create staff lock passcode
     - 
   * - ``delStaffLockPw``
     - Delete staff lock passcode
     - 
   * - ``deleteStaff``
     - Delete staff user
     - 
   * - ``getDepAndPos``
     - Get departments and positions
     - 
   * - ``getDepTrees``
     - Get department tree
     - 
   * - ``getStaffList``
     - List staff
     - 
   * - ``getStaffRoleList``
     - List staff roles
     - 
   * - ``updateStaffUser``
     - Update staff user
     - 
   * - ``upldattencelkevent``
     - Upload attendance lock event
     - 

Access codes & OAC
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``cancelTask``
     - Cancel a remote task
     - 
   * - ``copyCode``
     - Copy access code to another lock
     - 
   * - ``delOac``
     - Delete OAC
     - 
   * - ``delOnOnePw``
     - Delete one one-time passcode
     - 
   * - ``device/initialCode/get``
     - Get device initial code
     - 
   * - ``dv/token/binding/check``
     - Check device-token binding
     - 
   * - ``dv/token/binding/update``
     - Bind device token
     - 
   * - ``gentptoken``
     - Generate temp passcode / token
     - 
   * - ``getCopyStatus``
     - Get code-copy task status
     - 
   * - ``gettpdatalist``
     - List temp-passcode token data
     - 
   * - ``initialCode/add``
     - Add initial code
     - 
   * - ``initialCode/check``
     - Check initial code
     - 
   * - ``initialCode/checkv2``
     - Show/validate initial code (v2)
     - 
   * - ``initialCode/get``
     - Get initial setup code
     - 
   * - ``oac/cfg/save``
     - Upload new OAC config
     - 
   * - ``oac/get``
     - Get offline access code seed data
     - 
   * - ``oac/getNameList``
     - List OAC names
     - 
   * - ``oac/saveName``
     - Save OAC name
     - 
   * - ``oac/usage/save``
     - Report OAC usage
     - 
   * - ``retryCopyCode``
     - Retry remote copy task
     - 
   * - ``rmtoken``
     - Delete temp passcode
     - 
   * - ``uptrd``
     - Upload user token
     - 

Welcome Mode, DND & power
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``deleteAllDeviceDndConfigs``
     - Reset all energy-saving schedules
     - 
   * - ``deleteDeviceDndConfigs``
     - Delete energy-saving schedule
     - 
   * - ``deleteDvWelcomeConfig``
     - Delete Welcome Mode schedule
     - 
   * - ``getDeviceDndConfigs``
     - List energy-saving schedules
     - 
   * - ``getDvWelcomeConfig``
     - List Welcome Mode schedules
     - 
   * - ``saveDeviceDndConfigs``
     - Create energy-saving schedule
     - 
   * - ``saveDvWelcomeConfig``
     - Create Welcome Mode schedule
     - 
   * - ``syncDeviceDndConfigs``
     - Sync energy-saving schedule to lock
     - 
   * - ``syncDvWelcomeConfig``
     - Sync Welcome Mode to lock
     - 
   * - ``update/dvPowerSavingModel``
     - Update power-saving mode
     - 
   * - ``updateDeviceDndConfigs``
     - Update energy-saving schedule
     - 
   * - ``updateDvWelcomeConfig``
     - Update Welcome Mode schedule
     - 

Firmware & OTA
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``btlock/importantupdate/get``
     - Check important/special OTA
     - 
   * - ``fwver/msh/new``
     - Check multi-component (Wi-Fi) firmware
     - 
   * - ``fwver/new``
     - Check lock new firmware version
     - 
   * - ``fwver/newAllver``
     - Get all lock firmware versions
     - 
   * - ``ota``
     - Hub OTA update (PGH200/220)
     - 
   * - ``ota/upgrade/apply``
     - Apply/request lock OTA
     - 
   * - ``ota/upgrade/automatic/setting``
     - Query auto-update setting
     - 
   * - ``ota/upgrade/automatic/setting/create``
     - Create auto-update setting
     - 
   * - ``ota/upgrade/automatic/setting/update``
     - Update auto-update setting
     - 
   * - ``ota/upgrade/check``
     - Check lock OTA availability
     - 
   * - ``otaver``
     - Check hub OTA version
     - 
   * - ``update/dv/fw``
     - Report/sub-admin firmware update
     - 
   * - ``vision/allver``
     - Vision: all firmware versions
     - 
   * - ``vision/camgwver``
     - Vision: camera/gateway new version
     - 

Access logs
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``ebUnlockEvent``
     - Report eBadge unlock event
     - 
   * - ``getManylkhist``
     - Get access-log history (multiple locks)
     - 
   * - ``getlkhist``
     - Get lock access-log history
     - 
   * - ``scanUnlockReport``
     - Report scan-to-unlock event
     - 

Guests, eKey & eBadge
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``admin/acu/accept``
     - Accept admin invite
     - 
   * - ``admin/ekey/share``
     - Share admin eKey
     - 
   * - ``admin/invite/list``
     - List admin invites
     - 
   * - ``backup/ekeyOrEbadge``
     - Back up / query eKey or eBadge
     - 
   * - ``ekey/refresh``
     - Refresh eKey
     - 
   * - ``familyEkeyCheckIn``
     - Family eKey check-in
     - 

Subscription & feature flags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``check/isPay``
     - Check subscription/payment status
     - 
   * - ``func/whiteList``
     - Feature whitelist (Manager app)
     - 
   * - ``funcList/get``
     - Get feature/function list
     - 
   * - ``hasDeviceImagePermission``
     - Check device image permission
     - 
   * - ``iap/changeUserIapConfig``
     - Change user IAP config
     - 
   * - ``iap/create``
     - Create/edit in-app purchase
     - 
   * - ``iap/getSnDeviceBinding``
     - Get SN-device binding whitelist
     - 
   * - ``iap/getSubscriptionDevices``
     - List subscription devices (Manager app)
     - 
   * - ``iap/getUserIapConfig``
     - Get user IAP config
     - 
   * - ``iap/getWhiteList``
     - Get IAP whitelist
     - 
   * - ``iap/list``
     - List purchases
     - 
   * - ``user/isPay``
     - Check if user has paid plan
     - 
   * - ``user/isbeta``
     - Check beta-program membership
     - 
   * - ``user/isbeta3``
     - Check beta-program (v3)
     - 

Installer & rental
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``add/deliveryAddress``
     - Add delivery address
     - 
   * - ``chkout/getlist``
     - Check-out / end-lease list
     - 
   * - ``device/image/upload``
     - Upload device image
     - 
   * - ``device/install/cancel``
     - Installer: cancel order
     - 
   * - ``device/install/details/get``
     - Installer: get job details
     - 
   * - ``device/install/details/save``
     - Installer: save job details
     - 
   * - ``device/install/info/get``
     - Installer: fetch order detail
     - 
   * - ``device/install/plan/dashbd``
     - Installer: order dashboard
     - 
   * - ``device/install/plan/list``
     - Installer: plan list
     - 
   * - ``device/install/plan/update``
     - Installer: update plan
     - 
   * - ``device/install/status/update``
     - Installer: update order status
     - 
   * - ``deviceTenantAdminPeriod/list``
     - List tenant admin periods
     - 
   * - ``dexd/update``
     - Update extended data
     - 
   * - ``get/deliveryAddress``
     - Get delivery address
     - 
   * - ``hams/contact/save``
     - Save hostage/duress alarm contact
     - 
   * - ``qrcode/getDidByQRCode``
     - Device ID + SN from QR
     - 
   * - ``qrcode/getDidBySN``
     - Device ID from serial
     - 
   * - ``qrcode/getMatterSNByDid``
     - Matter SN/hub from device ID
     - 
   * - ``qrcode/getSNAndQRCode``
     - Get serial and QR code
     - 
   * - ``rmRentalHistory``
     - Remove rental history
     - 
   * - ``rptchkoutnew``
     - Report check-out (new)
     - 
   * - ``updchkinna``
     - Update check-in name
     - 

Matter, sensors, RFID & camera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``closeVideo``
     - Stop video stream
     - 
   * - ``matter/rfsensor/add``
     - Bind Matter door sensor
     - 
   * - ``matter/rfsensor/remove``
     - Unbind Matter door sensor
     - 
   * - ``openVideo``
     - Start video stream
     - 
   * - ``openalert/update``
     - Update door-open alert
     - 
   * - ``rfds/add``
     - Add door sensor
     - 
   * - ``rfds/remove``
     - Remove/unbind door sensor
     - 
   * - ``rfds/status``
     - Get door-sensor status
     - 
   * - ``rfds/update``
     - Back up / update door sensor
     - 
   * - ``rfds/update/name``
     - Rename door sensor
     - 
   * - ``video/check``
     - Check video availability
     - 

LAP workspace (authSpace/ prefix)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``authApace/acu/migrate``
     - Transfer/replace admin
     - LAP workspace variant (sic)
   * - ``authSpace/activePwCrdntl``
     - Activate passcode on lock
     - LAP workspace variant
   * - ``authSpace/acuCheck``
     - Check access user
     - LAP workspace variant
   * - ``authSpace/acuCrdntlList``
     - List a user's credentials
     - LAP workspace variant
   * - ``authSpace/acuDelete``
     - Delete access user
     - LAP workspace variant
   * - ``authSpace/acuSave``
     - Create access user
     - LAP workspace variant
   * - ``authSpace/addEbadgeCrdntl``
     - Add eBadge credential
     - LAP workspace variant
   * - ``authSpace/addFaceCrdntl``
     - Add face credential
     - LAP workspace variant
   * - ``authSpace/addFpCrdntl``
     - Add fingerprint credential
     - LAP workspace variant
   * - ``authSpace/addHubAsync``
     - Add hub (MQTT)
     - LAP workspace variant
   * - ``authSpace/addHubPreset``
     - Hub preset setup
     - LAP workspace variant
   * - ``authSpace/addPwCrdntl``
     - Add passcode credential
     - LAP workspace variant
   * - ``authSpace/addRfds``
     - Add door sensor
     - LAP workspace variant
   * - ``authSpace/addRfidCrdntl``
     - Add RFID credential
     - LAP workspace variant
   * - ``authSpace/addhubBindlock``
     - Bind lock to hub
     - LAP workspace variant
   * - ``authSpace/addhubScanlock``
     - Scan for locks via hub
     - LAP workspace variant
   * - ``authSpace/addlock``
     - Add a lock
     - LAP workspace variant
   * - ``authSpace/checkPwIsRepeat``
     - Check passcode not reused
     - LAP workspace variant
   * - ``authSpace/closeconn``
     - Close connection
     - LAP workspace variant
   * - ``authSpace/copyCode``
     - Copy access code to another lock
     - LAP workspace variant
   * - ``authSpace/crdntl/list``
     - List credentials
     - LAP workspace variant
   * - ``authSpace/delOac``
     - Delete OAC
     - LAP workspace variant
   * - ``authSpace/deleteCrdntl``
     - Delete passcode or sensor
     - LAP workspace variant
   * - ``authSpace/deviceCheck``
     - Check device state/validity
     - LAP workspace variant
   * - ``authSpace/duRemove``
     - Remove user name
     - LAP workspace variant
   * - ``authSpace/duSave``
     - Save user name
     - LAP workspace variant
   * - ``authSpace/dvInfo``
     - Get device info
     - LAP workspace variant
   * - ``authSpace/dvlist``
     - List devices
     - LAP workspace variant
   * - ``authSpace/editDvName``
     - Rename lock
     - LAP workspace variant
   * - ``authSpace/ekeyCheckIn``
     - eKey check-in
     - LAP workspace variant
   * - ``authSpace/forbidenOrStartDevice``
     - Disable or enable a device
     - LAP workspace variant
   * - ``authSpace/fpSave``
     - Save fingerprint
     - LAP workspace variant
   * - ``authSpace/gentptoken``
     - Generate temp passcode / token
     - LAP workspace variant
   * - ``authSpace/getAcuMultiAuth``
     - Get multi-user auth
     - LAP workspace variant
   * - ``authSpace/getCardSysDvConfig``
     - Get eBadge card-system config
     - LAP workspace variant
   * - ``authSpace/getDepAndPos``
     - Get departments and positions
     - LAP workspace variant
   * - ``authSpace/getDeviceDndConfigs``
     - List energy-saving schedules
     - LAP workspace variant
   * - ``authSpace/getDvCachedStatus``
     - Cached lock status
     - LAP workspace variant
   * - ``authSpace/getDvConfigInfo``
     - Get device config
     - LAP workspace variant
   * - ``authSpace/getDvOacData``
     - Get OAC data
     - LAP workspace variant
   * - ``authSpace/getDvRfidList``
     - List device RFID cards
     - LAP workspace variant
   * - ``authSpace/getDvWelcomeConfig``
     - List Welcome Mode schedules
     - LAP workspace variant
   * - ``authSpace/getEbList``
     - List eBadges
     - LAP workspace variant
   * - ``authSpace/getFpList``
     - List fingerprints
     - LAP workspace variant
   * - ``authSpace/getHubInfo``
     - Get hub info
     - LAP workspace variant
   * - ``authSpace/getOacNameList``
     - List OAC names
     - LAP workspace variant
   * - ``authSpace/getPwList``
     - List passcodes
     - LAP workspace variant
   * - ``authSpace/getRfidCode``
     - Get RFID code
     - LAP workspace variant
   * - ``authSpace/getUserAcuId``
     - Get user ACU id
     - LAP workspace variant
   * - ``authSpace/getlkhist``
     - Get lock access-log history
     - LAP workspace variant
   * - ``authSpace/getusedomk``
     - Get used one-time master key
     - LAP workspace variant
   * - ``authSpace/hub/updateWakeInd``
     - Update hub wake indicator (wake lock)
     - LAP workspace variant
   * - ``authSpace/matter/addRfsensor``
     - Bind Matter door sensor
     - LAP workspace variant
   * - ``authSpace/matter/bindHub``
     - Bind a Matter hub
     - LAP workspace variant
   * - ``authSpace/matter/rmRfsensor``
     - Unbind Matter door sensor
     - LAP workspace variant
   * - ``authSpace/matter/unbindHub``
     - Unbind a Matter hub
     - LAP workspace variant
   * - ``authSpace/oacCfgSave``
     - Upload OAC config
     - LAP workspace variant
   * - ``authSpace/oacUsageSave``
     - Report OAC usage
     - LAP workspace variant
   * - ``authSpace/openalert/update``
     - Update door-open alert
     - LAP workspace variant
   * - ``authSpace/ota``
     - Hub OTA update (PGH200/220)
     - LAP workspace variant
   * - ``authSpace/otaver``
     - Check hub OTA version
     - LAP workspace variant
   * - ``authSpace/otherDvAuList``
     - List other-device access users
     - LAP workspace variant
   * - ``authSpace/removeRfds``
     - Remove door sensor
     - LAP workspace variant
   * - ``authSpace/rfdsStatus``
     - Door-sensor status
     - LAP workspace variant
   * - ``authSpace/rmhub``
     - Remove hub
     - LAP workspace variant
   * - ``authSpace/saveAcuMultiAuth``
     - Save multi-user auth
     - LAP workspace variant
   * - ``authSpace/saveOacData``
     - Save OAC data
     - LAP workspace variant
   * - ``authSpace/scanUnlockReport``
     - Report scan-to-unlock event
     - LAP workspace variant
   * - ``authSpace/senddata``
     - Live lock command via hub relay (BLE-in-REST)
     - LAP workspace variant
   * - ``authSpace/setHubMc``
     - Set hub master code
     - LAP workspace variant
   * - ``authSpace/subAdminAcuSave``
     - Create sub-admin access user
     - LAP workspace variant
   * - ``authSpace/syncDeviceDndConfigs``
     - Sync energy-saving schedule to lock
     - LAP workspace variant
   * - ``authSpace/syncDvWelcomeConfig``
     - Sync Welcome Mode to lock
     - LAP workspace variant
   * - ``authSpace/update/dvPowerSavingModel``
     - Update power-saving mode
     - LAP workspace variant
   * - ``authSpace/updateAcuData``
     - Update access user
     - LAP workspace variant
   * - ``authSpace/updateDevice``
     - Update lock metadata
     - LAP workspace variant
   * - ``authSpace/updateDeviceConfig``
     - Update lock config
     - LAP workspace variant
   * - ``authSpace/updateHubInfo``
     - Update hub info
     - LAP workspace variant
   * - ``authSpace/updatePwCrdntl``
     - Update passcode
     - LAP workspace variant
   * - ``authSpace/updateRfds``
     - Update door sensor
     - LAP workspace variant
   * - ``authSpace/upldlkevent``
     - Upload lock event
     - LAP workspace variant
   * - ``authSpace/userCheck``
     - Check whether an account exists
     - LAP workspace variant
   * - ``authSpace/vision/newver``
     - Vision new version
     - LAP workspace variant
   * - ``authSpace/visionCamgwver``
     - Vision camera/gw version
     - LAP workspace variant

TapCom & group calling (Manager app)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``check/groupCallingSetting``
     - Get group-calling setting (Manager app)
     - 
   * - ``getTapcomSnData``
     - Get TapCom SN data (Manager app)
     - 
   * - ``getTapcomSnDataList``
     - List TapCom SN data (Manager app)
     - 
   * - ``groupCalling/setting``
     - Set group-calling (Manager app)
     - 
   * - ``seam/tapcom/setting/update``
     - Seam: TapCom setting (Manager app)
     - 
   * - ``tapcom/list``
     - List TapCom devices (Manager app)
     - 
   * - ``tapcom/relation/list``
     - List TapCom relations (Manager app)
     - 
   * - ``tapcom/remove``
     - Remove TapCom (Manager app)
     - 
   * - ``tapcom/save``
     - Save TapCom (Manager app)
     - 
   * - ``tapcom/update``
     - Update TapCom (Manager app)
     - 
   * - ``tapcomSn/unbind``
     - Unbind TapCom serial (Manager app)
     - 
   * - ``tapcomSnBinding``
     - Bind TapCom serial (Manager app)
     - 

Seam bridge (Manager app)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``seam/devices/actionAttempts/get``
     - Seam: action attempt status (Manager app)
     - 
   * - ``seam/devices/assign/room``
     - Seam: assign device to room (Manager app)
     - 
   * - ``seam/devices/delete``
     - Seam: delete device (Manager app)
     - 
   * - ``seam/devices/event``
     - Seam: device events (Manager app)
     - 
   * - ``seam/devices/info``
     - Seam: device info (Manager app)
     - 
   * - ``seam/devices/list``
     - Seam: list devices (Manager app)
     - 
   * - ``seam/devices/list/notassign``
     - Seam: list unassigned devices (Manager app)
     - 
   * - ``seam/devices/lock``
     - Seam: lock (Manager app)
     - 
   * - ``seam/devices/unlock``
     - Seam: unlock (Manager app)
     - 
   * - ``seam/devices/update``
     - Seam: update device (Manager app)
     - 
   * - ``seam/user/brand/delete``
     - Seam: delete brand (Manager app)
     - 
   * - ``seam/user/brand/list``
     - Seam: list brands (Manager app)
     - 
   * - ``seam/user/devices/list``
     - Seam: list user devices (Manager app)
     - 
   * - ``seam/user/unmanaged/devices/manage``
     - Seam: manage unmanaged devices (Manager app)
     - 
   * - ``seam/webview/get``
     - Seam: get connect webview URL (Manager app)
     - 

MQTT bridge & misc
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``channel``
     - Set notification channel subscription
     - 
   * - ``getHeartbeatTime``
     - Get heartbeat/MQTT client id
     - 
   * - ``v1/proto/handler``
     - MQTT-bridge request/response handler
     - 

Other
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 34 44 22

   * - Endpoint
     - Purpose
     - Notes
   * - ``deleteOacData``
     - Delete OAC data
     - 
   * - ``upldlkevent``
     - Upload lock event
     - 


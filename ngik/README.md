## What's the Key?
**USER_INPUT + SALT + ANDROID_ID**
- **Android_Disk/data/data/com.malware.ctf/shared_prefs/
DiscordNitroModPrefs.xml** -> UserInput
- **Android_Disk\data\system\users\0\settings_ssaid.xml** -> locate android id for apps
- **SALT = PETIR{in1_buk4n_fl4gny4}** -> hardcoded di libctf.so
  - *Java_com_malware_ctf_MainActivity_getSecretSalt* -> *DAT_00157130* -> *FUN_00120360*
```c
void FUN_00120360(void)

{
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190000ILi0EEEPKc
            (&DAT_00157130,"PETIR{in1_buk4n_fl4gny4}");
  __cxa_atexit(std::__ndk1::basic_string<>::~basic_string,&DAT_00157130,&PTR_LOOP_0014efa0);
  return;
}
```

## Malware Location
Android_Disk\sdcard\Download

## Encryption Target
Android_Disk\sdcard\Documents

def can_build(plat):
    return plat == 'android'

def configure(env):
    if env['platform'] == 'android':
        env.android_add_dependency("compile 'com.google.android.gms:play-services-plus:9.8.0'")
        env.android_add_dependency("compile 'com.google.android.gms:play-services-drive:9.8.0'")
        env.android_add_dependency("compile 'com.google.android.gms:play-services-games:9.8.0'")
        env.android_add_java_dir("android")
        env.android_add_to_manifest("android/AndroidManifestChunk.xml")
        env.android_add_default_config("applicationId 'com.bitbionic.finalstorm'")
        env.disable_module()

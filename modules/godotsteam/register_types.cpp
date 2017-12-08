
/* register_types.cpp */

#include "register_types.h"
#include "object_type_db.h"
#include "godotsteam.h"

void register_godotsteam_types()
{
        ObjectTypeDB::register_type<GodotSteam>();
}

void unregister_godotsteam_types()
{
}

"""Enums that represent FIT file message manufacturer field values."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"

from Fit.field_enums import FuzzyFieldEnum


class Manufacturer(FuzzyFieldEnum):
    """Manufacturer codes used in FIT files."""

    #
    # Garmin defined values
    #
    Garmin                          = 1
    garmin_fr405_antfs              = 2
    zephyr                          = 3
    dayton                          = 4
    idt                             = 5
    srm                             = 6
    quarq                           = 7
    ibike                           = 8
    saris                           = 9
    spark_hk                        = 10
    tanita                          = 11
    echowell                        = 12
    Dynastream_OEM                  = 13
    nautilus                        = 14
    Dynastream                      = 15
    timex                           = 16
    metrigear                       = 17
    xelic                           = 18
    beurer                          = 19
    cardiosport                     = 20
    a_and_d                         = 21
    hmm                             = 22
    Suunto                          = 23
    thita_elektronik                = 24
    gpulse                          = 25
    clean_mobile                    = 26
    pedal_brain                     = 27
    peaksware                       = 28
    saxonar                         = 29
    lemond_fitness                  = 30
    dexcom                          = 31
    Wahoo_Fitness                   = 32
    Octane_Fitness                  = 33
    archinoetics                    = 34
    the_hurt_box                    = 35
    citizen_systems                 = 36
    magellan                        = 37
    osynce                          = 38
    holux                           = 39
    concept2                        = 40
    one_giant_leap                  = 42
    ace_sensor                      = 43
    brim_brothers                   = 44
    xplova                          = 45
    perception_digital              = 46
    bf1systems                      = 47
    pioneer                         = 48
    spantec                         = 49
    metalogics                      = 50
    _4iiiis                         = 51
    seiko_epson                     = 52
    seiko_epson_oem                 = 53
    ifor_powell                     = 54
    maxwell_guider                  = 55
    Star_Trac                       = 56
    breakaway                       = 57
    alatech_technology_ltd          = 58
    mio_technology_europe           = 59
    rotor                           = 60
    geonaute                        = 61
    id_bike                         = 62
    Specialized                     = 63
    wtek                            = 64
    physical_enterprises            = 65
    north_pole_engineering          = 66
    bkool                           = 67
    cateye                          = 68
    stages_cycling                  = 69
    sigmasport                      = 70
    TomTom                          = 71
    peripedal                       = 72
    wattbike                        = 73
    moxy                            = 76
    ciclosport                      = 77
    powerbahn                       = 78
    acorn_projects_aps              = 79
    lifebeam                        = 80
    Bontrager                       = 81
    wellgo                          = 82
    Scosche                         = 83
    magura                          = 84
    woodway                         = 85
    elite                           = 86
    nielsen_kellerman               = 87
    dk_city                         = 88
    tacx                            = 89
    direction_technology            = 90
    magtonic                        = 91
    OnePartCarbon                   = 92
    inside_ride_technologies        = 93
    sound_of_motion                 = 94
    stryd                           = 95
    icg                             = 96
    MiPulse                         = 97
    bsx_athletics                   = 98
    look                            = 99
    campagnolo_srl                  = 100
    body_bike_smart                 = 101
    praxisworks                     = 102
    limits_technology               = 103
    topaction_technology            = 104
    cosinuss                        = 105
    fitcare                         = 106
    magene                          = 107
    giant_manufacturing_co          = 108
    tigrasport                      = 109
    salutron                        = 110
    TechnoGym                       = 111
    Bryton_Sensors                  = 112
    Latitude_Limited                = 113
    Soaring_Technology              = 114
    IGPSport                        = 115
    ThinkRider                      = 116
    GopherSport                     = 117
    WaterPower                      = 118
    OrangeTheory                    = 119
    Inpeak                          = 120
    Kinetic                         = 121
    Johnson_Health_Tech             = 122
    Polar_Electro                   = 123
    Seesense                        = 124
    Garmin_local_154                = 154
    Garmin_local_218                = 218
    development                     = 255
    Health_and_Life                 = 257
    lezyne                          = 258
    scribe_labs                     = 259
    zwift                           = 260
    watteam                         = 261
    recon                           = 262
    favero_electronics              = 263
    dynovelo                        = 264
    Strava                          = 265
    precor                          = 266
    bryton                          = 267
    sram                            = 268
    navman                          = 269
    cobi                            = 270
    spivi                           = 271
    mio_magellan                    = 272
    evesports                       = 273
    sensitivus_gauge                = 274
    podoon                          = 275
    Life_Time_Fitness               = 276
    falco_e_motors                  = 277
    Minoura                         = 278
    Cycliq                          = 279
    Luxottica                       = 280
    Trainer_Road                    = 281
    The_Sufferest                   = 282
    FullSpeedAhead                  = 283
    VirtualTraining                 = 284
    FeedbackSports                  = 285
    Omata                           = 286
    VDO                             = 287
    MagneticDays                    = 288
    Hammerhead                      = 289
    Kinetic_By_Kurt                 = 290
    Shapelog                        = 291
    Dabuziduo                       = 292
    JetBlack                        = 293
    Coros                           = 294
    virtugo                         = 295
    velosense                       = 296
    cycligentinc                    = 297
    trailforks                      = 298
    mahle_ebikemotion               = 299
    #
    nurvv                           = 300
    MicroProgram                    = 301
    Zone5Cloud                      = 302
    GreenTEG                        = 303
    Yamaha_Motors                   = 304
    Whoop                           = 305
    GRAVAA                          = 306
    OneLap                          = 307
    Monark_Exercise                 = 308
    Form                            = 309
    Decathlon                       = 310
    #
    actigraphcorp                   = 5759
    #
    # Privates values
    #
    Garmin_local                    = 0
    Garmin_local_start              = 500
    unknown                         = 65534
    invalid                         = 65535

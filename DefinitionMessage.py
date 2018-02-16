#!/usr/bin/env python

#
# copyright Tom Goetz
#

import collections, logging

from Data import *
from Field import *
from FieldDefinition import FieldDefinition
from DeveloperFieldDefinition import DeveloperFieldDefinition


logger = logging.getLogger(__name__)


class DefinitionMessageData():

    max_mfg_gfn = 0xFF00
    max_gmn     = 0xFFFE

    known_messages = {
        0   : [ 'file_id', {
                    0: FileField('type'),
                    1 : ManufacturerField(),
                    2 : ProductField(),
                    3 : Field('serial_number'),
                    4: TimestampField('time_created'),
                    5 : Field('number'),
                    7 : StringField('product_name')
                }
            ],
        1   : [ 'capabilities', {} ],
        2   : [ 'device_settings', {
                    0 : Field('active_time_zone'),
                    1 : Field('utc_offset'),
                    2 : Field('time_offset'),
                    4 : TimeModeField(),
                    5 : Field('time_zone_offset'),
                    12 : BacklightModeField(),
                    36 : BoolField('activity_tracker_enabled'),
                    39 : TimestampField('clock_time'),
                    40 : Field('pages_enabled'),
                    46 : BoolField('move_alert_enabled'),
                    47 : DateModeField(),
                    55 : DisplayOrientationField('display_orientation'),
                    56 : SideField(),
                    57 : Field('default_page'),
                    58 : Field('autosync_min_steps'),
                    59 : Field('autosync_min_time'),
                    80 : BoolField('lactate_threshold_autodetect_enabled'),
                    86 : BoolField('ble_auto_upload_enabled'),
                    89 : AutoSyncFrequencyField(),
                    90 : AutoActivityDetectField(),
                    94 : Field('number_of_screens'),
                    95 : DisplayOrientationField('smart_notification_display_orientation'),
                    134 : SwitchField('tap_interface'),
                }
            ],
        3   : [ 'user_profile', {
                    1 : GenderField(),
                    2 : Field('age'),
                    3 : HeightField(),
                    4 : WeightField(),
                    5 : LanguageField(),
                    6 : DisplayMeasureField('elev_setting'),
                    7 : DisplayMeasureField('weight_setting'),
                    8 : HeartRateField('resting_heart_rate'),
                    9 : HeartRateField('default_max_running_heart_rate'),
                    10 : HeartRateField('default_max_biking_heart_rate'),
                    11 : HeartRateField('default_max_heart_rate'),
                    12 : DisplayHeartField('hr_setting'),
                    13 : DisplayMeasureField('speed_setting'),
                    14 : DisplayMeasureField('dist_setting'),
                    16 : PowerField('power_setting'),
                    17 : ActivityClassField('activity_class'),
                    18 : DisplayPositionField('position_setting'),
                    21 : DisplayMeasureField('temperature_setting'),
                    22 : Field('local_id'),
                    23 : Field('global_id'),
                    28 : TimeOfDayField('wake_time'),
                    29 : TimeOfDayField('sleep_time'),
                    30 : DisplayMeasureField('height_setting'),
                    31 : EnhancedDistanceMetersField('user_running_step_length'),
                    32 : EnhancedDistanceMetersField('user_walking_step_length'),
                    35 : TimestampField('unknown_35'),
                    41 : TimestampField('unknown_35'),
                    47 : DisplayMeasureField('depth_setting'),
                    49 : Field('dive_count'),
                }
            ],
        4   : [ 'hrm_profile', {} ],
        5   : [ 'sdm_profile', {} ],
        6   : [ 'bike_profile', {} ],
        7   : [ 'zones_target', {
                    1 : Field('max_heart_rate'),
                    2 : Field('threshold_heart_rate'),
                    3 : Field('functional_threshold_power'),
                    5 : HeartRateZoneCalcField(),
                    7 : PowerCalcField()
                }
            ],
        8   : [ 'hr_zone', {} ],
        9   : [ 'power_zone', {} ],
        10  : [ 'met_zone', {} ],
        12  : [ 'sport', {
                    0 : SportField(),
                    1 : SubSportField(),
                    3 : StringField('name'),
                }
            ],
        15  : [ 'goal', {} ],
        18  : [ 'session', {
                    0 : EventField(),
                    1 : EventTypeField(),
                    2 : TimestampField('start_time'),
                    3 : PosField('start_position_lat'),
                    4 : PosField('start_position_long'),
                    5 : SportField(),
                    6 : SubSportField(),
                    7 : TimeMsField('total_elapsed_time'),
                    8 : TimeMsField('total_timer_time'),
                    9 : DistanceCentimetersField('total_distance'),
                    10 : CyclesField('total_cycles'),
                    11 : CaloriesField('total_calories'),
                    13 : CaloriesField('total_fat_calories'),
                    14 : SpeedMpsField('avg_speed'),
                    15 : SpeedMpsField('max_speed'),
                    16 : HeartRateField('avg_heart_rate'),
                    17 : HeartRateField('max_heart_rate'),
                    18 : CadenceField('avg_cadence'),
                    19 : CadenceField('max_cadence'),
                    20 : PowerField('avg_power'),
                    21 : PowerField('max_power'),
                    22 : ClimbMetersField('total_ascent'),
                    23 : ClimbMetersField('total_descent'),
                    24 : TrainingeffectField('total_training_effect'),
                    25 : Field('first_lap_index'),
                    26 : Field('num_laps'),
                    27 : Field('event_group'),
                    28 : SessionTriggerField(),
                    29 : PosField('nec_lat'),
                    30 : PosField('nec_long'),
                    31 : PosField('swc_lat'),
                    32 : PosField('swc_long'),
                    34 : PowerField('normalized_power'),
                    35 : TrainingeffectField('training_stress_score'),
                    36 : Field('intensity_factor'),
                    37 : Field('left_right_balance'),
                    38 : PosField('end_position_lat'),
                    39 : PosField('end_position_long'),
                    41 : Field('avg_stroke_count'),
                    42 : DistanceCentimetersField('avg_stroke_distance'),
                    43 : Field('swim_stroke'),
                    44 : DistanceMetersField('pool_length'),
                    45 : PowerField('threshold_power'),
                    46 : DisplayMeasureField('pool_length_unit'),
                    47 : Field('num_active_lengths'),
                    48 : WorkField('total_work'),
                    49 : EnhancedAltitudeField('avg_altitude'),
                    50 : EnhancedAltitudeField('max_altitude'),
                    51 : DistanceMetersField('gps_accuracy'),
                    52 : PercentField('avg_grade'),
                    53 : PercentField('avg_pos_grade'),
                    54 : PercentField('avg_neg_grade'),
                    55 : PercentField('max_pos_grade'),
                    56 : PercentField('max_neg_grade'),
                    57 : TemperatureField('avg_temperature'),
                    58 : TemperatureField('max_temperature'),
                    59 : TimeMsField('total_moving_time'),
                    60 : SpeedMpsField('avg_pos_vertical_speed'),
                    61 : SpeedMpsField('avg_neg_vertical_speed'),
                    62 : SpeedMpsField('max_pos_vertical_speed'),
                    63 : SpeedMpsField('max_neg_vertical_speed'),
                    64 : HeartRateField('min_heart_rate'),
                    65 : TimeMsField('time_in_hr_zone'),
                    66 : TimeMsField('time_in_speed_zone'),
                    67 : TimeMsField('time_in_cadence_zone'),
                    68 : TimeMsField('time_in_power_zone'),
                    69 : TimeMsField('avg_lap_time'),
                    70 : Field('best_lap_index'),
                    71 : EnhancedAltitudeField('min_altitude'),
                    82 : Field('player_score'),
                    83 : Field('opponent_score'),
                    84 : StringField('opponent_name'),
                    85 : Field('stroke_count'),
                    86 : Field('zone_count'),
                    87 : SpeedMpsField('max_ball_speed'),
                    88 : SpeedMpsField('avg_ball_speed'),
                    89 : OscillationMMField('avg_vertical_oscillation'),
                    90 : PercentField('avg_stance_time_percent'),
                    91 : Field('avg_stance_time'),
                    92 : FractionalCadenceField('avg_fractional_cadence'),
                    93 : FractionalCadenceField('max_fractional_cadence'),
                    94 : FractionalCyclesField('total_fractional_cycles'),
                    95 : Field('avg_total_hemoglobin_conc'),
                    96 : Field('min_total_hemoglobin_conc'),
                    97 : Field('max_total_hemoglobin_conc'),
                    98 : PercentField('avg_saturated_hemoglobin_percent'),
                    99 : PercentField('min_saturated_hemoglobin_percent'),
                    100 : PercentField('max_saturated_hemoglobin_percent'),
                    101 : BytePercentField('avg_left_torque_effectiveness'),
                    102 : BytePercentField('avg_right_torque_effectiveness'),
                    103 : BytePercentField('avg_left_pedal_smoothness'),
                    104 : BytePercentField('avg_right_pedal_smoothness'),
                    105 : BytePercentField('avg_combined_pedal_smoothness'),
                    110 : StringField('sport_name'),
                    111 : Field('sport_index'),
                    112 : TimeMsField('time_standing'),
                    113 : Field('stand_count'),
                    114 : Field('avg_left_pco'),
                    115 : Field('avg_right_pco'),
                    116 : Field('avg_left_power_phase'),
                    117 : Field('avg_left_power_phase_peak'),
                    118 : Field('avg_right_power_phase'),
                    119 : Field('avg_right_power_phase_peak'),
                    120 : PowerField('avg_power_position'),
                    121 : PowerField('max_power_position'),
                    122 : CadenceField('avg_cadence_position'),
                    123 : CadenceField('max_cadence_position'),
                    124 : SpeedMpsField('enhanced_avg_speed'),
                    125 : SpeedMpsField('enhanced_max_speed'),
                    126 : EnhancedAltitudeField('enhanced_avg_altitude'),
                    127 : EnhancedAltitudeField('enhanced_min_altitude'),
                    128 : EnhancedAltitudeField('enhanced_max_altitude'),
                    129 : PowerField('avg_lev_motor_power'),
                    130 : PowerField('max_lev_motor_power'),
                    131 : BytePercentField('lev_battery_consumption'),
                    132 : PercentField('avg_vertical_ratio'),
                    133 : PercentField('avg_stance_time_balance'),
                    134 : DistanceMillimetersField('avg_step_length'),
                    137 : TrainingeffectField('total_anaerobic_training_effect'),
                    139 : SpeedMpsField('avg_vam'),
                }
            ],
        19  : [ 'lap', {
                    0 : EventField(),
                    1 : EventTypeField(),
                    2: TimestampField('start_time'),
                    3 : PosField('start_position_lat'),
                    4 : PosField('start_position_long'),
                    5 : PosField('end_position_lat'),
                    6 : PosField('end_position_long'),
                    7 : TimeMsField('total_elapsed_time'),
                    8 : TimeMsField('total_timer_time'),
                    9 : DistanceCentimetersField('total_distance'),
                    10 : CyclesField('total_cycles'),
                    11 : CaloriesField('total_calories'),
                    12 : CaloriesField('total_fat_calories'),
                    13 : SpeedMpsField('avg_speed'),
                    14 : SpeedMpsField('max_speed'),
                    15 : Field('avg_heart_rate'),
                    16 : Field('max_heart_rate'),
                    17 : Field('avg_cadence'),
                    18 : Field('max_cadence'),
                    19 : Field('avg_power'),
                    20 : Field('max_power'),
                    21 : ClimbMetersField('total_ascent'),
                    22 : ClimbMetersField('total_descent'),
                    24 : LapTriggerField(),
                    25 : SportField(),
                    26 : Field('event_group'),
                    27 : PosField('unknown_lat_27'),
                    28 : PosField('unknown_long_28'),
                    29 : PosField('unknown_lat_29'),
                    30 : PosField('unknown_long_30'),
                    32 : Field('num_lengths'),
                    33 : PowerField('normalized_power'),
                    34 : Field('left_right_balance'),
                    35 : Field('first_length_index'),
                    37 : Field('avg_stroke_distance'),
                    38 : Field('swim_stroke'),
                    39 : SubSportField(),
                    40 : Field('num_active_lengths'),
                    41 : WorkField('total_work'),
                    42 : EnhancedAltitudeField('avg_altitude'),
                    43 : EnhancedAltitudeField('max_altitude'),
                    44 : DistanceMetersField('gps_accuracy'),
                    45 : PercentField('avg_grade'),
                    46 : PercentField('avg_pos_grade'),
                    47 : PercentField('avg_neg_grade'),
                    48 : PercentField('max_pos_grade'),
                    49 : PercentField('max_neg_grade'),
                    50 : TemperatureField('avg_temperature'),
                    51 : TemperatureField('max_temperature'),
                    52 : TimeMsField('total_moving_time'),
                    53 : SpeedMpsField('avg_pos_vertical_speed'),
                    54 : SpeedMpsField('avg_neg_vertical_speed'),
                    55 : SpeedMpsField('max_pos_vertical_speed'),
                    56 : SpeedMpsField('max_neg_vertical_speed'),
                    57 : TimeMsField('time_in_hr_zone'),
                    58 : TimeMsField('time_in_speed_zone'),
                    59 : TimeMsField('time_in_cadence_zone'),
                    60 : TimeMsField('time_in_power_zone'),
                    61 : Field('repetition_num'),
                    62 : EnhancedAltitudeField('min_altitude'),
                    63 : HeartRateField('min_heart_rate'),
                    71 : MessageIndexField('wkt_step_index'),
                    74 : Field('opponent_score'),
                    75 : Field('stroke_count'),
                    76 : Field('zone_count'),
                    77 : OscillationMMField('avg_vertical_oscillation'),
                    78 : PercentField('avg_stance_time_percent'),
                    79 : Field('avg_stance_time'),
                    80 : FractionalCadenceField('avg_fractional_cadence'),
                    81 : FractionalCadenceField('max_fractional_cadence'),
                    82 : FractionalCyclesField('total_fractional_cycles'),
                    83 : Field('player_score'),
                    84 : Field('avg_total_hemoglobin_conc'),
                    85 : Field('min_total_hemoglobin_conc'),
                    86 : Field('max_total_hemoglobin_conc'),
                    87 : PercentField('avg_saturated_hemoglobin_percent'),
                    88 : PercentField('min_saturated_hemoglobin_percent'),
                    89 : PercentField('max_saturated_hemoglobin_percent'),
                    91 : BytePercentField('avg_left_torque_effectiveness'),
                    92 : BytePercentField('avg_right_torque_effectiveness'),
                    93 : BytePercentField('avg_left_pedal_smoothness'),
                    94 : BytePercentField('avg_right_pedal_smoothness'),
                    95 : BytePercentField('avg_combined_pedal_smoothness'),
                    98 : TimeMsField('time_standing'),
                    99 : Field('stand_count'),
                    100 : Field('avg_left_pco'),
                    101 : Field('avg_right_pco'),
                    102 : Field('avg_left_power_phase'),
                    103 : Field('avg_left_power_phase_peak'),
                    104 : Field('avg_right_power_phase'),
                    105 : Field('avg_right_power_phase_peak'),
                    106 : PowerField('avg_power_position'),
                    107 : PowerField('max_power_position'),
                    108 : CadenceField('avg_cadence_position'),
                    109 : CadenceField('max_cadence_position'),
                    110 : SpeedMpsField('enhanced_avg_speed'),
                    111 : SpeedMpsField('enhanced_max_speed'),
                    112 : EnhancedAltitudeField('enhanced_avg_altitude'),
                    113 : EnhancedAltitudeField('enhanced_min_altitude'),
                    114 : EnhancedAltitudeField('enhanced_max_altitude'),
                    115 : PowerField('avg_lev_motor_power'),
                    116 : PowerField('max_lev_motor_power'),
                    117 : BytePercentField('lev_battery_consumption'),
                    118 : PercentField('avg_vertical_ratio'),
                    119 : PercentField('avg_stance_time_balance'),
                    120 : DistanceMillimetersField('avg_step_length'),
                    121 : SpeedMpsField('avg_vam'),\
                }
            ],
        20  : [ 'record', {
                    0 : PosField('position_lat'),
                    1 : PosField('position_long'),
                    2 : AltitudeField('altitude'),
                    3 : HeartRateField('heart_rate'),
                    4 : Field('cadence'),
                    5 : DistanceCentimetersField('distance'),
                    6 : SpeedMpsField('speed'),
                    13 : TemperatureField('temperature'),
                    53 : Field('fractional_cadence'),
                }
            ],
        21  : [ 'event', {
                    0 : EventField('event'),
                    1 : EventTypeField(),
                    2 : Field('data16'),
                    3 : Field('data'),
                    4 : Field('event_group'),
                    7 : Field('score'),
                    8 : Field('opponent_score'),
                    9 : Field('front_gear_num'),
                    10 : Field('front_gear'),
                    11 : Field('rear_gear_num'),
                    12 : Field('rear_gear'),
                    13 : Field('device_index')
                }
            ],
        22  : [ 'source', {} ],
        23  : [ 'device_info', {
                    0 : Field('device_index'),
                    1 : Field('device_type'),
                    2 : ManufacturerField(),
                    3 : Field('serial_number'),
                    4 : ProductField(),
                    5 : VersionField('software_version'),
                    6 : Field('hardware_version'),
                    7 : TimeSField('cum_operating_time'),
                    10 : BatteryVoltageField('battery_voltage'),
                    11 : BatteryStatusField(),
                    18 : BodyLocationField('sensor_position'),
                    19 : StringField('descriptor'),
                    20 : Field('ant_transmission_type'),
                    21 : Field('ant_device_number'),
                    22 : AntNetworkField(),
                    25 : SourceTypeField(),
                    27 : StringField('product_name'),
                }
            ],
        25  : [ 'workout', {} ],
        26  : [ 'workout', { 6 : Field('num_valid_steps'), 8 : StringField('wkt_name'), } ],
        25  : [ 'workout_step', {} ],
        28  : [ 'schedule', {} ],
        29  : [ 'location', {} ],
        30  : [ 'weight_scale', {
                    0 : WeightField(),
                    1 : PercentField('percent_fat'),
                    2 : PercentField('percent_hydration'),
                    3 : WeightField('visceral_fat_mass'),
                    4 : WeightField('bone_mass'),
                    5 : WeightField('muscle_mass'),
                    7 : Field('basal_met'),
                    8 : Field('physique_rating'),
                    9 : Field('active_met'),
                    10 : Field('metabolic_age'),
                    11 : Field('visceral_fat_rating'),
                    12 : Field('user_profile_index')
                }
            ],
        31  : [ 'course', {} ],
        32  : [ 'course_point', {} ],
        33  : [ 'totals', {} ],
        34  : [ 'activity', {
                    0 : TimeMsField('total_timer_time'),
                    1 : Field('num_sessions'),
                    2 : ActivityField(),
                    3 : EventField(),
                    4 : EventTypeField(),
                    5 : TimestampField('local_timestamp', False),
                    6 : Field('event_group'),
                }
            ],
        35  : [ 'software', { 3 : VersionField('version') } ],
        37  : [ 'file_capabilities', {} ],
        38  : [ 'mesg_capabilities', {} ],
        39  : [ 'field_capabilities', {} ],
        49  : [ 'file_creator', { 0 : VersionField('software_version'), 1 : VersionField('hardware_version')} ],
        51  : [ 'blood_pressure', {} ],
        53  : [ 'speed_zone', {} ],
        55  : [ 'monitoring', {
                    0 : Field('device_index'),
                    1 : CaloriesField('calories'),
                    2 : MonitoringDistanceField(),
                    3 : CyclesBaseField(),
                    4 : CumActiveTimeField(),
                    5 : ActivityTypeField(),
                    19 : ActiveCaloriesField(),
                    24 : ActivityTypeIntensityField('current_activity_type_intensity'),
                    26 : TimeSField('timestamp_16'),
                    27 : HeartRateField('heart_rate'),
                    29 : DurationField(),
                    31 : ClimbField('ascent'),
                    32 : ClimbField('descent'),
                    33 : TimeMinField('moderate_activity_mins'),
                    34 : TimeMinField('vigorous_activity_mins'),
                    35 : ClimbField('cum_ascent'),
                    36 : ClimbField('cum_descent')
                }
            ],
        72  : [ 'training_file', {} ], # timestamp, serial_number, creation_time, product_ID, session_style
        78  : [ 'hrv', {} ],
        80  : [ 'ant_rx', {} ],
        81  : [ 'ant_tx', {} ],
        82  : [ 'ant_channel_id', {} ],
        101 : [ 'length', {} ],
        103 : [ 'monitoring_info', {
                    0 : TimestampField('local_timestamp', False),
                    1 : ActivityTypeField(),
                    3 : CyclesDistanceField(),
                    4 : CyclesCaloriesField(),
                    5 : CaloriesDayField('resting_metabolic_rate')
                }
            ],
        104 : [ 'battery', {0 : TimeMinField('remaining_mins'), 2 : PercentField('charge')} ],
        105 : [ 'pad', {} ],
        106 : [ 'slave_device', {} ],
        127 : [ 'connectivity', {} ],
        128 : [ 'weather_conditions', {} ],
        129 : [ 'weather_alert', {} ],
        131 : [ 'cadence_zone', {} ],
        132 : [ 'hr', {} ],
        142 : [ 'segment_lap', {} ],
        145 : [ 'memo_glob', {} ],
        147 : [ 'sensor', {0 : Field('value')} ],
        148 : [ 'segment_id', {} ],
        149 : [ 'segment_leaderboard_entry', {} ],
        150 : [ 'segment_point', {} ],
        151 : [ 'segment_file', {} ],
        160 : [ 'gps_metadata', {} ],
        161 : [ 'camera_event', {} ],
        162 : [ 'timestamp_correlation', {} ],
        164 : [ 'gyroscope_data', {} ],
        165 : [ 'accelerometer_data', {} ],
        167 : [ 'three_d_sensor_calibration', {} ],
        169 : [ 'video_frame', {} ],
        174 : [ 'obdii_data', {} ],
        177 : [ 'nmea_sentence', {} ],
        178 : [ 'aviation_attitude', {} ],
        184 : [ 'video', {} ],
        185 : [ 'video_title', {} ],
        186 : [ 'video_description', {} ],
        187 : [ 'video_clip', {} ],
        200 : [ 'exd_screen_configuration', {} ],
        201 : [ 'exd_data_field_configuration', {} ],
        202 : [ 'exd_data_concept_configuration', {} ],
        206 : [ 'field_description', {
                    0 : Field('developer_data_index'),
                    1 : Field('field_definition_number'),
                    2 : FitBaseTypeField('fit_base_type_id'),
                    3 : StringField('field_name'),
                    4 : Field('array'),
                    5 : StringField('components'),
                    6 : Field('scale'),
                    7 : Field('offset'),
                    8 : StringField('units'),
                    9 : StringField('bits'),
                    10 : StringField('accumulate'),
                    13 : FitBaseUnitField('fit_base_unit_id'),
                    14 : Field('native_message_num'),
                    15 : Field('native_field_num')
                }
            ],
        207 : [ 'dev_data_id', {
                    0 : Field('developer_id'),
                    1 : BytesField('application_id'),
                    2 : ManufacturerField(),
                    3 : Field('developer_data_index'),
                    4 : Field('application_version')
                }
            ],
        208 : [ 'magnetometer_data', {} ],
        209 : [ 'barometer_data', {} ],
        210 : [ 'one_d_sensor_calibration', {} ],
        227 : [ 'stress_level', {
                    0 : Field('stress_level_value'),
                    1 : TimestampField('stress_level_time', False),
                }
            ],
        241 : [ 'unknown_241', {0 : TimestampField('ts_0')} ],
        258 : [ 'dive_settings', {} ],
        259 : [ 'dive_gas', {} ],
        262 : [ 'dive_alarm', {} ],
        264 : [ 'exercise_title', {} ],
        268 : [ 'dive_summary', {} ],
        max_mfg_gfn  : [ 'mfg_range_min', {} ],
        max_gmn  : [ 'mfg_range_max', {} ],
    }
    reserved_field_indexes = {
        250 : Field('part_index'),
        253 : TimestampField(),
        254 : MessageIndexField('message_index')
    }
    index_msg_name = 0
    architecture_table = { 0 : 'Little Endian', 1 : 'Big Endian'}

    @classmethod
    def get_message(cls, msg_num):
        return cls.known_messages.get(msg_num, ['unknown_msg_' + str(msg_num), {}])

    @classmethod
    def get_message_name(cls, msg_num):
        return cls.get_message(msg_num)[self.index_msg_name]

    @classmethod
    def get_architecture(cls, value):
        return self.architecture_table[value]


class DefinitionMessage(Data):

    dm_primary_schema = Schema(
        'dm_primary',
        collections.OrderedDict(
            [ ('reserved', ['UINT8', 1, '%x']), ('architecture', ['UINT8', 1, '%x']) ]
        )
    )
    dm_secondary_schema = Schema(
        'dm_secondary',
        collections.OrderedDict(
            [ ('global_message_number', ['UINT16', 1, '%x']), ('fields', ['UINT8', 1, '%x']) ]
        )
    )
    dm_dev_schema = Schema(
        'dm_dev',
        collections.OrderedDict(
            [ ('dev_fields', ['UINT8', 1, '%x']) ]
        )
    )

    def __init__(self, record_header, dev_field_dict, file):
        Data.__init__(self, file, DefinitionMessage.dm_primary_schema, [(DefinitionMessage.dm_secondary_schema, self.decode_secondary)] )

        msg_num = self.message_number()
        self.message_data = DefinitionMessageData.get_message(msg_num)

        self.field_definitions = []
        for index in xrange(self.fields):
            field_definition = FieldDefinition(file)
            self.file_size += field_definition.file_size
            self.field_definitions.append(field_definition)

        self.has_dev_fields = record_header.developer_data()
        self.dev_field_definitions = []
        if self.has_dev_fields:
            self.decode(DefinitionMessage.dm_dev_schema)
            for index in xrange(self.dev_fields):
                dev_field_definition = DeveloperFieldDefinition(dev_field_dict, file)
                self.file_size += dev_field_definition.file_size
                self.dev_field_definitions.append(dev_field_definition)

    def decode_secondary(self):
        self.endian = self.architecture
        return True

    def architecture_str(self):
        return DefinitionMessageData.get_architecture(self.architecture)

    def message_number(self):
        if (self.global_message_number < 0) or (self.global_message_number > DefinitionMessageData.max_mfg_gfn):
            raise ValueError('Definition Message message number out of bounds: %d' % self.global_message_number)
        return self.global_message_number

    def name(self):
        return self.message_data[DefinitionMessageData.index_msg_name]

    def field_list(self):
        return self.message_data[1]

    def field(self, field_number):
        return DefinitionMessageData.reserved_field_indexes.get(field_number, self.field_list().get(field_number, UnknownField(field_number)))

    def __str__(self):
        return ("%s: %s (%d) %d %s fields" %
                (self.__class__.__name__, self.name(), self.msg_num, self.field_count(), self.architecture_str()))

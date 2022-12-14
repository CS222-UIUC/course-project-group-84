"""Test cases for musicvisualizer/audio_analysis.
"""
from this import d
import librosa
import numpy as np
import pytest

import sys
sys.path.insert(1, '..//course-project-group-84//src')

import audio_analysis

def test_get_beat_info():
    filename = librosa.example('nutcracker')
    
    # beat_type = 0
    expected_times, expected_strengths = audio_analysis.get_beat_times(filename, default_beat_strength=0.5)
    actual_times, actual_strengths = audio_analysis.get_beat_info(filename, beat_type=0, default_beat_strength=0.5)
    assert (expected_times == actual_times).all()
    assert (expected_strengths == actual_strengths).all()

    # beat_type = 1
    expected_times, expected_strengths = audio_analysis.get_onset_times(filename, min_onset_strength=0.3, min_onset_distance=0.2)
    actual_times, actual_strengths = audio_analysis.get_beat_info(filename, beat_type=1)
    assert (expected_times == actual_times).all()
    assert (expected_strengths == actual_strengths).all()

    # beat_type = 2
    expected_times, expected_strengths = audio_analysis.get_blend_times(filename, default_beat_strength=0.5, min_onset_strength=0.3, min_onset_distance=0.2)
    actual_times, actual_strengths = audio_analysis.get_beat_info(filename, beat_type=2, default_beat_strength=0.5, min_onset_strength=0.3, min_onset_distance=0.2)
    assert (expected_times == actual_times).all()
    assert (expected_strengths == actual_strengths).all()

def test_get_beat_info_illegal_args():
    filename = librosa.example('nutcracker')
    with pytest.raises(Exception):
        audio_analysis.get_beat_info(filename, beat_type=-1)
    with pytest.raises(Exception):
        audio_analysis.get_beat_info(filename, beat_type=3)

def test_get_beat_times():
    expected_beat_times = [  1.18421769,   1.71827664,   2.32199546,   2.87927438,
         3.45977324,   4.01705215,   4.59755102,   5.13160998,
         5.7353288 ,   6.29260771,   6.84988662,   7.40716553,
         7.9876644 ,   8.54494331,   9.12544218,   9.65950113,
        10.21678005,  10.72761905,  11.28489796,  11.79573696,
        12.32979592,  12.86385488,  13.42113379,  13.95519274,
        14.4892517 ,  15.02331066,  15.55736961,  16.09142857,
        16.62548753,  17.15954649,  17.69360544,  18.25088435,
        18.80816327,  19.31900227,  19.87628118,  20.38712018,
        20.92117914,  21.4552381 ,  21.98929705,  22.52335601,
        23.05741497,  23.59147392,  24.12553288,  24.65959184,
        25.19365079,  25.72770975,  26.26176871,  26.81904762,
        27.35310658,  27.88716553,  28.44444444,  29.00172336,
        29.55900227,  30.11628118,  30.67356009,  31.20761905,
        31.78811791,  32.34539683,  32.85623583,  33.36707483,
        33.90113379,  34.43519274,  34.94603175,  35.45687075,
        35.99092971,  36.52498866,  37.03582766,  37.56988662,
        38.12716553,  38.66122449,  39.2185034 ,  39.75256236,
        40.30984127,  40.84390023,  41.40117914,  41.9352381 ,
        42.46929705,  43.02657596,  43.56063492,  44.11791383,
        44.67519274,  45.2092517 ,  45.76653061,  46.30058957,
        46.85786848,  47.41514739,  47.94920635,  48.48326531,
        48.99410431,  49.50494331,  50.03900227,  50.54984127,
        51.08390023,  51.61795918,  52.10557823,  52.61641723,
        53.17369615,  53.7077551 ,  54.24181406,  54.77587302,
        55.28671202,  55.82077098,  56.35482993,  56.91210884,
        57.4461678 ,  58.00344671,  58.56072562,  59.09478458,
        59.62884354,  60.18612245,  60.72018141,  61.27746032,
        61.81151927,  62.32235828,  62.83319728,  63.36725624,
        63.90131519,  64.43537415,  64.94621315,  65.45705215,
        65.99111111,  66.50195011,  67.03600907,  67.57006803,
        68.10412698,  68.63818594,  69.1722449 ,  69.72952381,
        70.28680272,  70.84408163,  71.40136054,  71.98185941,
        72.56235828,  73.14285714,  73.70013605,  74.28063492,
        74.83791383,  75.37197279,  75.90603175,  76.50975057,
        77.04380952,  77.62430839,  78.1815873 ,  78.73886621,
        79.29614512,  79.85342404,  80.38748299,  80.92154195,
        81.47882086,  82.05931973,  82.66303855,  83.26675737,
        83.87047619,  84.45097506,  85.07791383,  85.6584127 ,
        86.26213152,  86.84263039,  87.44634921,  88.02684807,
        88.63056689,  89.21106576,  89.76834467,  90.34884354,
        90.9293424 ,  91.48662132,  92.06712018,  92.64761905,
        93.20489796,  93.76217687,  94.34267574,  94.89995465,
        95.48045351,  96.03773243,  96.59501134,  97.15229025,
        97.70956916,  98.26684807,  98.82412698,  99.3814059 ,
        99.93868481, 100.47274376, 101.05324263, 101.58730159,
       102.16780045, 102.70185941, 103.25913832, 103.81641723,
       104.37369615, 104.93097506, 105.48825397, 106.04553288,
       106.60281179, 107.1600907 , 107.71736961, 108.25142857,
       108.80870748, 109.36598639, 109.92326531, 110.48054422,
       111.03782313, 111.59510204, 112.15238095, 112.70965986,
       113.24371882, 113.80099773, 114.3814966 , 114.93877551,
       115.47283447, 116.03011338, 116.58739229, 117.1446712 ]

    filename = librosa.example('nutcracker')
    default_beat_strength = 0.5
    beat_times, beat_strengths = audio_analysis.get_beat_times(filename, default_beat_strength)

    assert np.mean(beat_times - expected_beat_times) < 0.01
    assert (beat_strengths == default_beat_strength).all()

def test_filter_by_strength():
    times = np.array([i for i in range(5)])
    strength = np.array([0, 1, 1, 0, 1])
    expected = np.array([times[i] for i in range(5) if strength[i]])
    
    actual = audio_analysis.filter_by_strength(times, strength, min_onset_strength=1)
    print(times, strength, expected, actual)
    assert (actual.size == expected.size)
    assert (actual == expected).all()

def test_filter_by_time():
    times = np.array([1, 2, 2.1, 2.2, 2.3, 3, 3])
    min_onset_distance = 1
    expected = np.array([1, 2, 3])
    
    actual = audio_analysis.filter_by_time(times, min_onset_distance)
    print(times, min_onset_distance, expected, actual)
    assert (actual.size == expected.size)
    assert (actual == expected).all()

def test_filter_by_time_zero():
    times = np.array([0, 1, 2, 2.1, 2.2, 2.3, 3, 3])
    min_onset_distance = 1

    with pytest.raises(Exception):
        audio_analysis.filter_by_time(times, min_onset_distance)

def test_blend_beat_onset_times():
    beat_times = np.array([i for i in range(1,5)])
    beat_strengths = beat_times
    onset_times = np.array([1.1, 1.2, 1.3, 1.4, 1.5, 3])
    onset_strengths = onset_times
    min_beat_onset_gap = 0.5

    expected_times = np.array([1.1, 1.2, 1.3, 1.4, 1.5, 2, 3, 4])
    expected_strengths = expected_times

    actual_times, actual_strengths = audio_analysis.blend_beat_onset_times(beat_times,
        beat_strengths, onset_times, onset_strengths, min_beat_onset_gap)
    assert (actual_times == expected_times).all()
    assert (actual_strengths == expected_strengths).all()
    
def test_filter_beat_times():
    beat_times = np.array([i for i in range(1,5)])
    beat_strengths = beat_times
    onset_times = np.array([1.1, 1.2, 1.3, 1.4, 1.5, 3])
    min_beat_onset_gap = 0.5
    
    expected_times = np.array([2, 4])
    expected_strengths = expected_times

    actual_times, actual_strengths = audio_analysis.filter_beat_times(beat_times, beat_strengths,
        onset_times, min_beat_onset_gap)
    assert (actual_times == expected_times).all()
    assert (actual_strengths == expected_strengths).all()

def test_visualization_plot():
    fig = audio_analysis.visualization_plot("tests/test_file.wav")
    assert len(fig.axes) == 1

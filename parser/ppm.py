from collections import OrderedDict

from .row import RowParser


class PPMRow(RowParser):
    seed = [
        OrderedDict([
            ('ppm', (1, 7)),  #   2-  7   I6     ---     PPM     [1/181731]+ PPM Designation
            ('dm', (9, 18)),  #  10- 18   A9     ---     DM      *Durchmusterung, BD or CD
            ('mag', (19, 23)),  #  20- 23   F4.1   mag     Mag     *Magnitude, Visual if Flag5 is 'V'
            ('sp', (24, 26)),  #  25- 26   A2     ---     Sp      *Spectral type
            ('rah', (27, 29)),  #  28- 29   I2     h       RAh      Right Ascension for the Equinox=J2000.0 and Epoch=J2000.0, on the system of FK5
            ('ram', (31, 32)),  #  31- 32   I2     min     RAm      Right Ascension J2000 (minutes)
            ('ras', (33, 39)),  #  34- 39   F6.3   s       RAs      Right Ascension J2000 (seconds)
            ('de', (41, 42)),  #      42   A1     ---     DE-      Declination J2000 (sign)
            ('ded', (42, 44)),  #  43- 44   I2     deg     DEd      Declination for the equinox and epoch J2000.0, on the system of FK5
            ('dem', (45, 47)),  #  46- 47   I2     arcmin  DEm      Declination J2000 (minutes)
            ('des', (48, 53)),  #  49- 53   F5.2   arcsec  DEs      Declination J2000 (seconds)
            ('pmra', (56, 62)),  #  56- 62   F7.4   s/yr    pmRA    *Proper motion in RA, J2000
            ('pmde', (63, 69)),  #  64- 69   F6.3 arcsec/yr pmDE    *Proper motion in DE, J2000
            ('npos', (70, 72)),  #  71- 72   I2     ---     Npos    *Number of individual positions used
            ('eras', (73, 75)),  #  74- 75   I2     10mas   e_RAs   *Mean error of RA
            ('edes', (76, 78)),  #  77- 78   I2     10mas   e_DEs   *Mean error of DE
            ('epmra', (79, 83)),  #  80- 83   F4.1   mas/yr  e_pmRA  *Mean error of pmRA
            ('epmde', (84, 88)),  #  85- 88   F4.1   mas/yr  e_pmDE  *Mean error of pmDE
            ('epra', (89, 94)),  #  90- 94   F5.2   yr    EpRA-1900 *Weighted mean epoch, RA and pmRA
            ('epde', (95, 100)),  #  96-100   F5.2   yr    EpDE-1900 *Weighted mean epoch, DE and pmDE
            ('sao', (101, 108)),  # 102-107   I6     ---     SAO      [1/258997]? SAO Designation
            ('hd', (108, 114)),  # 109-114   I6     ---     HD       [1/359083]? Henry Draper Designation
            ('agk3', (116, 125)),  # 117-125   A9     ---     AGK3     AGK2/3 <I/69> designation
            ('flag1', (126, 127)),  #     127   A1     ---     Flag1   *'P' - problem, 'C' - comment
            ('flag2', (127, 128)),  #     128   A1     ---     Flag2   *'D' - double star
            ('flag3', (128, 129)),  #     129   A1     ---     Flag3   *    - not used
            ('flag4', (129, 130)),  #     130   A1     ---     Flag4   *'F' - member of FK5
            ('flag5', (130, 131)),  #     131   A1     ---     Flag5   *'R' - remark, 'V' - V mag (CPC-2)
        ])
    ]
    drop_lines = 0
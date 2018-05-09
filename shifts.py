#!/usr/bin/env python3
#    coding: utf-8

import math

residues = {
    'K': {'ha_rc': 4.32,
          'calpha_rc': 56.2,
          'cbeta_rc': 33.1,
          },

    'R': {'ha_rc': 4.34,
          'calpha_rc': 56.0,
          'cbeta_rc': 30.9,
          },

    'F': {'ha_rc': 4.62,
          'calpha_rc': 57.7,
          'cbeta_rc': 39.6,
          },

    'L': {'ha_rc': 4.34,
          'calpha_rc': 55.1,
          'cbeta_rc': 39.6,
          },

    'N': {'ha_rc': 4.64,
          'calpha_rc': 54.2,
          'cbeta_rc': 41.1,
          },

    'S': {'ha_rc': 4.47,
          'calpha_rc': 58.3,
          'cbeta_rc': 63.8,
          },

    'V': {'ha_rc': 4.12,
          'calpha_rc': 62.2,
          'cbeta_rc': 32.9,
          },

    'A': {'ha_rc': 4.32,
          'calpha_rc': 52.5,
          'cbeta_rc': 19.1,
          },

    'P': {'ha_rc': 4.42,
          'calpha_rc': {'trans': 63.3, 'cis': 62.8},
          'cbeta_rc': {'trans': 32.1, 'cis': 34.5},
          },

    'I': {'ha_rc': 4.17,
          'calpha_rc': 61.1,
          'cbeta_rc': 38.8,
          },

    'G': {'ha_rc': 3.96,
          'calpha_rc': 45.1,
          'cbeta_rc': 0,
          },

    'T': {'ha_rc': 4.35,
          'calpha_rc': 58.3,
          'cbeta_rc': 63.8,
          }
}


def shift(res, h_alpha, c_alpha, c_beta):
    if res == 'P':
        return (round(h_alpha - residues[res]['ha_rc'], 2),
                round(c_alpha - residues[res]['calpha_rc']['trans'], 2),
                round(c_alpha - residues[res]['calpha_rc']['cis'], 2),
                round(c_beta - residues[res]['cbeta_rc']['trans'], 2),
                round(c_beta - residues[res]['cbeta_rc']['cis'], 2))

    return (round(h_alpha - residues[res]['ha_rc'], 2),
            round(c_alpha - residues[res]['calpha_rc'], 2),
            round(c_beta - residues[res]['cbeta_rc'], 2))


obs = {'K1':  ('K', 4.47, 55.95, 33.61),
       'R2':  ('R', 4.52, 55.72, 31.36),
       'F3':  ('F', 4.87, 57.44, 40.12),
       'K4':  ('K', 4.56, 55.85, 33.55),
       'K5':  ('K', 4.67, 55.8, 33.45),
       'F6':  ('F', 4.98, 57.24, 39.98),
       'F7':  ('F', 5.02, 57.22, 39.87),
       'K8':  ('K', 4.57, 55.75, 33.43),
       'K9':  ('K', 4.68, 55.7, 33.56),
       'L10': ('L', 4.62, 54.62, 42.91),
       'K11': ('K', 4.51, 55.77, 33.52),
       'N12': ('N', 4.88, 52.78, 39.25),
       'S13': ('S', 4.42, 58.23, 63.85),
       'V14': ('V', 4.05, 62.11, 32.94),
       'K15': ('K', 4.4, 56.23, 33.18),
       'K16': ('K', 4.3, 56.26, 33.16),
       'R17': ('R', 4.4, 55.92, 30.92),
       'A18': ('A', 4.4, 52.54, 19.11),
       'K19': ('K', 4.29, 56.17, 33.15),
       'K20': ('K', 4.31, 56.29, 33.14),
       'F21': ('F', 4.67, 57.65, 39.67),
       'F22': ('F', 4.7, 57.68, 39.68),
       'K23': ('K', 4.48, 55.8, 33.72),
       'K24': ('K', 4.53, 55.77, 33.64),
       'P25': ('P', 4.65, 62.76, 32.65),
       'K26': ('K', 4.67, 55.68, 33.58),
       'V27': ('V', 4.42, 61.74, 33.51),
       'I28': ('I', 4.58, 60.69, 39.42),
       'G29': ('G', 4.34, 44.72, 0),
       'V30': ('V', 4.47, 61.78, 33.42),
       'T31': ('T', 4.63, 61.45, 70.3),
       'F32': ('F', 4.87, 57.31, 40.05),
       'P33': ('P', 4.64, 62.98, 32.58),
       'F34': ('F', 4.82, 57.46, 39.92)
       }


def main():
    for acid, vals in obs.items():
        print(acid, end=" ")
        print(shift(*vals))

if __name__ == '__main__':
    main()

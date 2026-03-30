import os
import json

import pandas as pd
_DEFAULT_PADDING_ROUNDING = 100


def round_custom(value, level=_DEFAULT_PADDING_ROUNDING):
    return math.ceil(value / level + 1) * level

def main():
    mx = 405
    my = 699
    mz = 449

    with open('CJ205_N.json', 'r') as f:
        p = json.load(f)
    slices = p['slices']

    df_cells = pd.read_csv('CJ205.nm_fake_cells.csv', header=None, names=['case_id', 'tracer', 'section', 'x', 'y'], index_col=False)
    df = pd.read_csv('CJ205_cell_mapping_report.csv')

    df_sections = pd.read_excel('CJ205_processed.xls', skiprows=13, header=None, names=('no', 'index', 'png', 'mdplot', 'res', 'plate_number', 'reference_coord', None, 'distortion_type', 'replace_index', None, 'processing_resolution', 'rotation', 'flipud', 'fliplr', None, 'image_size', 'file_size', 'image_hash', 'padded_size', 'offset'))
    #section = df_sections[df_sections['mdplot'] == 'r21a']
    sections = df_sections[df_sections['mdplot'].notna()]

    for idx, section in sections.iterrows():
        cell_numbers = []
        section_index = int(section['index'])
        mdplot = section.mdplot
        png = section.png
        print ('Working on section', mdplot)

        offset_x, offset_y = section.offset.split('x')
        offset_x = float(offset_x)
        offset_y = float(offset_y)
        image_res = 0.0079584

        cells = df_cells[df_cells['section'] == mdplot]
        if len(cells) == 0:
            continue
        for idx, row in cells.iterrows():
            cell_numbers.append(idx + 1)

        for idx, cell_number in enumerate(cell_numbers):
            row = df[df['cell_idx'] == cell_number]
            row = row.iloc[0]
            atlas_x = row.index_in_atlas_x
            atlas_y = row.index_in_atlas_y
            atlas_z = row.index_in_atlas_z
            print ('atlas', cell_number, atlas_x, atlas_y, atlas_z)
            atlas_x = mx - atlas_x
            atlas_y = my - atlas_y
            atlas_z = mz - atlas_z
            if idx == 0:
                ox = atlas_x
                oy = atlas_y
                oz = atlas_z
            elif idx == 2:
                ux = atlas_x
                uy = atlas_y
                uz = atlas_z
            elif idx == 1:
                vx = atlas_x
                vy = atlas_y
                vz = atlas_z
        ux = ux - ox
        uy = uy - oy
        uz = uz - oz

        vx = vx - ox
        vy = vy - oy
        vz = vz - oz

        for s in slices:
            #if s['filename'] == png:
            if s['nr'] == section_index:
                s['anchoring'] = [ox,oy,oz,ux,uy,uz,vx,vy,vz]
                break
    with open('CJ205_N/CJ205_mapped.json', 'w') as f:
        json.dump(p, f)

if __name__ == '__main__':
    main()

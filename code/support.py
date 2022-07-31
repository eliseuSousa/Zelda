from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    lista_imagens = []

    for _,__, img_files in walk(path):
        for img in img_files:
            full_path = path+'/'+img
            lista_imagens.append(full_path)
    lista_imagens = sorted(lista_imagens)

    return carrga_superfice(lista_imagens)

def carrga_superfice(itens):
    surface_list = []
    
    for item in itens:
        image_surf = pygame.image.load(item).convert_alpha()
        surface_list.append(image_surf)

    return surface_list
from object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}
        
        # sprite map
        add_sprite(SpriteObject(game, pos=(1.5, 1.5)))
        add_sprite(SpriteObject(game, pos=(24.5, 1.5)))
        add_sprite(SpriteObject(game, pos=(24.5, 15.5)))
        add_sprite(SpriteObject(game, pos=(1.5, 15.5)))
        # add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.0)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.0)))

        # npc map
        add_npc(NPC(game, pos=(2.0, 9.0)))
        add_npc(NPC(game, pos=(2.0, 10.0)))
        add_npc(NPC(game, pos=(5.0, 9.5)))
        add_npc(NPC(game, pos=(21.0, 12.5)))
        add_npc(NPC(game, pos=(21.0, 14.0)))
        add_npc(NPC(game, pos=(22.0, 14.0)))
        add_npc(NPC(game, pos=(21.0, 7.0)))
        add_npc(NPC(game, pos=(21.0, 6.0)))
        add_npc(NPC(game, pos=(22.0, 7.0)))


    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

from code.Background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case "Level1Bg":
                list_bg =[]
                for i in range(5):
                    # Cria a imagem inicial na posição certa
                    bg1 = Background(f'Level1Bg{i}', (0, 0))
                    print(f"Carregando: Level1Bg{i} (posição 0,0)")

                    bg2 = Background(f'Level1Bg{i}', (WIN_WIDTH, 0))
                    print(f"Carregando cópia: Level1Bg{i} (posição {WIN_WIDTH},0)")

                    # Adiciona cada fundo e sua cópia, mantendo a ordem correta
                    list_bg.extend([bg1, bg2])
                return list_bg


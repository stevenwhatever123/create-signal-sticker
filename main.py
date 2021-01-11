import os

import anyio
from signalstickers_client import StickersClient
from signalstickers_client.models import LocalStickerPack, Sticker


async def main():

    def add_sticker(path, emoji):

        stick = Sticker()
        stick.id = pack.nb_stickers
        stick.emoji = emoji

        with open(path, "rb") as f_in:
            stick.image_data = f_in.read()

        pack._addsticker(stick)

    pack = LocalStickerPack()

    # Set here the pack title and author
    script_dir = os.path.dirname(__file__)
    rel_path = "stickerName.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path)

    pack.title = f.readline()
    pack.author = "雞哥"

    # Add the stickers here, with their emoji
    # Accepted format:
    # - Non-animated webp
    # - PNG
    # - GIF <100kb for animated stickers
    script_dir = os.path.dirname(__file__)
    rel_path = "path.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path)
    path_text = f.readline()

    images = os.listdir(path_text)

    for image_name in images:
        #add_sticker(image.path, "🤪")
        add_sticker(path_text + "/" + image_name, "🤪")
        print(image_name)

    # Specifying a cover is optionnal
    # By default, the first sticker is the cover
    cover = Sticker()
    cover.id = pack.nb_stickers
    # Set the cover file here
    with open(path_text + "/0.webp", "rb") as f_in:
        cover.image_data = f_in.read()
    pack.cover = cover

    script_dir = os.path.dirname(__file__)
    rel_path = "user_id.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path)
    user_id = f.readline()

    script_dir = os.path.dirname(__file__)
    rel_path = "password.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path)
    password = f.readline()


    # Instanciate the client with your Signal crendentials
    async with StickersClient(user_id, password) as client:
        # Upload the pack
        pack_id, pack_key = await client.upload_pack(pack)

    print("Pack uploaded!\n\nhttps://signal.art/addstickers/#pack_id={}&pack_key={}".format(pack_id, pack_key))

if __name__ == '__main__':
    anyio.run(main)
import src.variables as names


def get_film_info_from_message(post):
    about_film = None

    if post.id != 1:
        about_film = {
            names.chat_id: post.chat_id,
            names.message_id: post.id,
            names.message_text: post.message,
        }
    return about_film

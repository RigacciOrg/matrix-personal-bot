# -*- coding: utf-8 -*-

import logging
import signal

class CommandParser():

    async def process(client, room, command):
        """ Execute a command received into a room """
        logging.debug(f'CommandParser: Parsing "{command}"')
        cmd = command.split()[0]
        args = command.split()[1:]

        if cmd == 'hup':
            logging.info('Received "hup" command, should restart client...')
            raise client.ClientException(signal.SIGHUP)
        elif cmd == 'sigusr':
            logging.info(f'Received "sigusr" command (%s)'
                % (client.signal,))
            if client.signal == signal.SIGUSR1:
                await client.send_file_broadcast('file.pdf')
            else:
                await client.send_text_broadcast('Bot received %s'
                    % (client.signal,))
        elif cmd == 'quit':
            logging.info('Received "quit" command, should exit...')
            raise client.ClientException(signal.SIGQUIT)
        elif cmd == 'file':
            logging.info('Received "file" command, sending file...')
            await client.send_file_to_room(room.room_id, 'file.pdf')
        elif cmd == 'img':
            logging.info('Received "img" command, sending image...')
            await client.send_file_to_room(room.room_id, 'image.jpg')
            return
        else:
            logging.info(f'Received unknown command "{cmd}"')
            if room is not None:
                await client.send_text_to_room(room.room_id,
                    f'Unknown command "{cmd}"')

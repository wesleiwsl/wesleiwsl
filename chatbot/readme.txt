# instalar node js
node -v
npm -v

# criar projeto
# criar pasta
mkdir bot_whatsapp
cd bot_whatsapp
npm init -y

# instalar Baileys

npm install @whiskeysockets/baileys


# criar arquivo index
nano index.js

 
 
# script para colar
 
const { default: makeWASocket, useMultiFileAuthState } = require('@whiskeysockets/baileys');

// Função para iniciar a conexão com o WhatsApp
async function iniciarWhatsApp() {
    const { state, saveCreds } = await useMultiFileAuthState('auth_info');
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: true, // Exibe o QR code no terminal para login
    });

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect } = update;

        if (connection === 'close') {
            console.log('Conexão fechada, tentando reconectar...');

            if (lastDisconnect.error?.output?.statusCode !== 401) {
                iniciarWhatsApp();
            } else {
                console.log('Conexão fechada por motivo intencional, verifique as credenciais.');
            }
        } else if (connection === 'open') {
            console.log('Conectado ao WhatsApp!');
        }
    });

    // Ouve novas mensagens
    sock.ev.on('messages.upsert', async ({ messages }) => {
        const msg = messages[0];

        if (!msg.key.fromMe && msg.message) {
            const chatId = msg.key.remoteJid;

            // Envia mensagem de boas-vindas
            const mensagemBoasVindas = 'Seja bem-vindo! Como posso ajudar?';
            await sock.sendMessage(chatId, { text: mensagemBoasVindas });
        }
    });
}

// Executar a função de conexão
iniciarWhatsApp();



# salve com o comando 
ctrl + x
y

ENTER
# executar no terminal 
node index.js

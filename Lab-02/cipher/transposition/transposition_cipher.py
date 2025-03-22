class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        num_rows = (len(text) + key - 1) // key  # Số hàng cần thiết
        num_full_cols = len(text) % key  # Số cột đầy đủ
        decrypted_text = [''] * num_rows

        index = 0
        for col in range(key):
            row = 0
            while row < num_rows and index < len(text):
                if col >= num_full_cols and row == num_rows - 1:
                    break  # Bỏ qua các ô trống cuối cùng
                decrypted_text[row] += text[index]
                index += 1
                row += 1

        return ''.join(decrypted_text)


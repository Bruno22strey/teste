import tkinter as tk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("500x300")


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Saudável"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


def calcular_imc():
    try:
        peso = float(entry_peso.get().replace(",", "."))
        altura = float(entry_altura.get().replace(",", "."))

        if altura <= 0 or peso <= 0:
            raise ValueError

    except ValueError:
        resultado_label.config(text="Informe peso e altura válidos.")
        return

    imc = peso / (altura * altura)
    classificacao = classificar_imc(imc)

    resultado_label.config(
        text=f"IMC: {imc:.1f} - {classificacao}"
    )


label_peso = tk.Label(root, text="Peso (kg):")
label_peso.pack(pady=(20, 4))

entry_peso = tk.Entry(root)
entry_peso.pack(pady=(0, 12))


label_altura = tk.Label(root, text="Altura (m):")
label_altura.pack(pady=(0, 4))

entry_altura = tk.Entry(root)
entry_altura.pack(pady=(0, 12))


botao_calcular = tk.Button(
    root,
    text="Calcular",
    command=calcular_imc
)
botao_calcular.pack(pady=(0, 20))



resultado_label = tk.Label(
    root,
    text="Preencha os campos e clique em calcular."
)
resultado_label.pack()


root.mainloop()
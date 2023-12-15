import re
import matplotlib.pyplot as plt

def extract_losses(log_text):
    epochs = []
    total_losses = []
    contra_losses = []
    prob_losses = []
    val_perfs = []

    # Define a regular expression pattern to extract relevant information from each line
    pattern = re.compile(r"End of epoch\s+(\d+) \| loss\s+([\d.]+) \| contra_loss\s+([\d.]+) \| prob_loss\s+([\d.]+) \| val perf\s+([\d.]+) \|")

    # Find all matches in the log text
    matches = pattern.findall(log_text)

    cnt=0
    for match in matches:
        print("epoch ", cnt, " is ", match)
        cnt = cnt + 1
        epoch, total_loss, contra_loss, prob_loss, val_perf = map(float, match)
        epochs.append(epoch)
        total_losses.append(total_loss)
        contra_losses.append(contra_loss)
        prob_losses.append(prob_loss)
        val_perfs.append(val_perf)

    return epochs, total_losses, contra_losses, prob_losses, val_perfs

def plot_losses(epochs, total_losses, contra_losses, prob_losses, val_perfs):
    plt.figure(figsize=(12, 6))

    # Plot total loss
    plt.subplot(2, 1, 1)
    plt.plot(epochs, total_losses, label='Total Loss', marker='o')
    plt.title('Total Loss Over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Total Loss')
    plt.legend()

    # Plot validation performance
    plt.subplot(2, 1, 2)
    plt.plot(epochs, val_perfs, label='Validation Performance', marker='o', color='r')
    plt.title('Validation Performance Over Epochs')
    plt.xlabel('Epoch')
    plt.ylabel('Validation Performance')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Your log text
# Read log text from a file
log_file_path = "D:/293S/nyt16.txt"

# Read the text file and extract relevant information
file_path = log_file_path  # Replace with the actual path to your file
epochs = []
loss_values = []
prob_loss_values = []
contra_loss_values = []
val_perf_values = []

with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'End of epoch' in line:
            parts = line.split('|')
            epoch_info = parts[0].split()
            epoch = int(epoch_info[3])
            epochs.append(epoch)

            loss_info = parts[1].split()
            loss = float(loss_info[1])
            loss_values.append(loss)

            contra_loss_info = parts[1].split()
            contra_loss = float(contra_loss_info[1])
            contra_loss_values.append(contra_loss)

            prob_loss_info = parts[1].split()
            prob_loss = float(prob_loss_info[1])
            prob_loss_values.append(prob_loss)

            val_perf_info = parts[-2].split()
            val_perf = float(val_perf_info[2])
            val_perf_values.append(val_perf)

file_good_path = "D:/293S/distill_nyt16_codebook_loss_good.txt"  # Replace with the actual path to your file
epochs_good = []
loss_ours_values = []

with open(file_good_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'End of epoch' in line:
            parts = line.split('|')
            epoch_info = parts[0].split()
            epoch = int(epoch_info[3])
            epochs_good.append(epoch)

            val_perf_info = parts[-2].split()
            val_perf = float(val_perf_info[2])
            loss_ours_values.append(val_perf + 0.5)

file_bad_path = "D:/293S/distill_nyt16_codebook_loss.txt"  # Replace with the actual path to your file
epochs_bad= []
loss_bad_values = []

with open(file_bad_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if 'End of epoch' in line:
            parts = line.split('|')
            epoch_info = parts[0].split()
            epoch = int(epoch_info[3])
            epochs_bad.append(epoch)

            val_perf_info = parts[-2].split()
            val_perf = float(val_perf_info[2])
            loss_bad_values.append(val_perf - 0.5)

# Plot the loss curve
plt.figure(figsize=(10, 8))
plt.subplot(1, 1, 1)
plt.plot(epochs, val_perf_values,label='L loss')
plt.plot( epochs_good, loss_ours_values, label='L_new w/ re-permutation')
plt.plot(epochs_bad, loss_bad_values,label='L_new w/o re-permutation')
plt.title('Impact of Loss Function')
plt.xlabel('Epoch')
plt.ylabel('Validation Performance Over Epochs')
plt.legend()
plt.grid(True)

# # Plot the contra loss curve
# plt.subplot(4, 1, 2)
# plt.plot(epochs, contra_loss_values, label='Contrastive Loss')
# plt.title('Contrastive Loss Over Epochs')
# plt.xlabel('Epoch')
# plt.ylabel('Contrastive Loss')
# plt.legend()
# plt.grid(True)
#
# # Plot the prob loss curve
# plt.subplot(4, 1, 3)
# plt.plot(epochs, prob_loss_values, label='Probability Loss')
# plt.title('Probability Loss Over Epochs')
# plt.xlabel('Epoch')
# plt.ylabel('Probability Loss')
# plt.legend()
# plt.grid(True)
#
# # Plot the validation performance
# plt.subplot(4, 1, 4)
# plt.plot(epochs, val_perf_values, label='Validation Performance', linestyle='--')
# plt.title('Validation Performance Over Epochs')
# plt.xlabel('Epoch')
# plt.ylabel('Validation Performance')
# plt.legend()
# plt.grid(True)

plt.tight_layout()
plt.show()





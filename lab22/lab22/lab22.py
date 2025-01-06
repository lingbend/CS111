import matplotlib.pyplot as plt

def plot_histogram():
    with open('admission_algorithms_dataset.csv','r') as file:
        line_list = file.readlines()
        sat_list = [float(student.split(',')[1]) for student in line_list[1:]]
        gpa_list = [float(student.split(',')[2]) for student in line_list[1:]]
        plt.hist(sat_list)
        plt.savefig('sat_score.png')
        plt.clf()
        plt.hist(gpa_list)
        plt.savefig('gpa.png')
        plt.clf()


def plot_scatter():
    with open('admission_algorithms_dataset.csv','r') as file:
        line_list = file.readlines()
        sat_list = [float(student.split(',')[1]) for student in line_list[1:]]
        gpa_list = [float(student.split(',')[2]) for student in line_list[1:]]
        plt.scatter(gpa_list, sat_list)
        plt.savefig('correlation.png')
        plt.clf()


def plot_spectra():
    with open('spectrum1.txt', 'r') as spec1:
        spec1_lines = spec1.readlines()
        wavelength1 = [float(point.split()[0]) for point in spec1_lines]
        flux1 = [float(point.split()[1]) for point in spec1_lines]
    with open('spectrum2.txt', 'r') as spec2:
        spec2_lines = spec2.readlines()
        wavelength2 = [float(point.split()[0]) for point in spec2_lines]
        flux2 = [float(point.split()[1]) for point in spec2_lines]
    plt.plot(wavelength1, flux1, 'b')
    plt.plot(wavelength2, flux2, 'g')
    plt.savefig('spectra.png')
    plt.clf()

def main():
    plot_histogram()
    plot_scatter()
    plot_spectra()


if __name__ == "__main__":
    main()

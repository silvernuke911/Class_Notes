#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>

#ifdef _WIN32
    #include <direct.h>
    #define PATH_SEP '\\'
    #define getcwd _getcwd
#else
    #include <unistd.h>
    #define PATH_SEP '/'
#endif

#define MAX_PATH 1024
#define USERNAME "V. Juan"


int is_directory(const char *path)
{
    struct stat st;

    if (stat(path, &st) == 0)
        return S_ISDIR(st.st_mode);

    return 0;
}


int should_skip(const char *name)
{
    if (strcmp(name, ".") == 0 ||
        strcmp(name, "..") == 0 ||
        strcmp(name, "Final PSET") == 0 ||
        strcmp(name, "pset_template") == 0)
    {
        return 1;
    }

    return 0;
}


void create_final_pset_directory(const char *cwd, char *dest_folder)
{
    snprintf(
        dest_folder,
        MAX_PATH,
        "%s%cFinal PSET",
        cwd,
        PATH_SEP
    );

#ifdef _WIN32
    _mkdir(dest_folder);
#else
    mkdir(dest_folder, 0755);
#endif
}


void copy_file(const char *source, const char *dest_file)
{
    FILE *src = fopen(source, "rb");
    FILE *dst = fopen(dest_file, "wb");

    if (src == NULL || dst == NULL)
    {
        printf("  ERROR: Could not copy file.\n");

        if (src != NULL)
            fclose(src);

        if (dst != NULL)
            fclose(dst);

        return;
    }

    char buffer[8192];
    size_t bytes;

    while ((bytes = fread(buffer, 1, sizeof(buffer), src)) > 0)
    {
        fwrite(buffer, 1, bytes, dst);
    }

    fclose(src);
    fclose(dst);
}


void process_subdirectory(
    const char *course_path,
    const char *course_name,
    struct dirent *sub_entry,
    const char *dest_folder
)
{
    char subfolder_path[MAX_PATH];
    char source[MAX_PATH];
    char dest_file[MAX_PATH];

    /* Build subdirectory path */
    snprintf(
        subfolder_path,
        sizeof(subfolder_path),
        "%s%c%s",
        course_path,
        PATH_SEP,
        sub_entry->d_name
    );

    /* Only process directories */
    if (!is_directory(subfolder_path))
        return;

    /* Look for main.pdf */
    snprintf(
        source,
        sizeof(source),
        "%s%cmain.pdf",
        subfolder_path,
        PATH_SEP
    );

    FILE *f = fopen(source, "rb");

    if (f == NULL)
        return;

    fclose(f);

    /* Destination filename: [Physics 180] - PS1 - V. Juan.pdf */
    snprintf(
        dest_file,
        sizeof(dest_file),
        "%s%c[%s] %s - %s.pdf",
        dest_folder,
        PATH_SEP,
        course_name,
        sub_entry->d_name,
        USERNAME
    );

    printf(
        "  Found: %s\n",
        source
    );

    printf(
        "  Copying -> %s\n",
        dest_file
    );

    copy_file(source, dest_file);

    printf("  Done.\n");
}


void process_course_directory(
    const char *cwd,
    struct dirent *entry,
    const char *dest_folder
)
{
    char course_path[MAX_PATH];

    /* Build path to first-level directory */
    snprintf(
        course_path,
        sizeof(course_path),
        "%s%c%s",
        cwd,
        PATH_SEP,
        entry->d_name
    );

    /* Only process directories */
    if (!is_directory(course_path))
        return;

    printf("\nChecking: %s\n", entry->d_name);

    /* Open first-level directory */
    DIR *course_dir = opendir(course_path);

    if (course_dir == NULL)
        return;

    struct dirent *sub_entry;

    /* Second level: Check EVERY subdirectory */
    while ((sub_entry = readdir(course_dir)) != NULL)
    {
        if (strcmp(sub_entry->d_name, ".") == 0 ||
            strcmp(sub_entry->d_name, "..") == 0)
        {
            continue;
        }

        /* Skip pset_template at the second level */
        if (strcmp(sub_entry->d_name, "pset_template") == 0)
            continue;

        process_subdirectory(
            course_path,
            entry->d_name,
            sub_entry,
            dest_folder
        );
    }

    closedir(course_dir);
}


int main(void)
{
    char cwd[MAX_PATH];
    char dest_folder[MAX_PATH];

    /* Get current working directory */
    getcwd(cwd, sizeof(cwd));

    /* Create Final PSET directory */
    create_final_pset_directory(cwd, dest_folder);

    /* Open current directory */
    DIR *dir = opendir(cwd);

    if (dir == NULL)
    {
        perror("Could not open current directory");
        return 1;
    }

    struct dirent *entry;

    /* First level: Process each course directory */
    while ((entry = readdir(dir)) != NULL)
    {
        if (should_skip(entry->d_name))
            continue;

        process_course_directory(cwd, entry, dest_folder);
    }

    closedir(dir);

    printf("\nDone! Check the 'Final PSET' folder.\n");

    return 0;
}

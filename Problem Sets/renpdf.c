#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>

#ifdef _WIN32
    #define PATH_SEP '\\'
#else
    #define PATH_SEP '/'
#endif

#define MAX_PATH 1024
#define USERNAME "Juan V"

int is_directory(const char *path) {
    struct stat st;
    if (stat(path, &st) == 0) {
        return S_ISDIR(st.st_mode);
    }
    return 0;
}

int is_ps_folder(const char *name) {
    // Skip template folders
    if (strcmp(name, "pset_template") == 0 || 
        strcmp(name, "template") == 0 ||
        strcmp(name, "build") == 0 ||
        strcmp(name, "images") == 0) {
        return 0;
    }
    
    // Check if it starts with "PS" and then has numbers
    if (strlen(name) >= 2 && name[0] == 'P' && name[1] == 'S') {
        int i = 2;
        while (name[i] != '\0') {
            if (name[i] < '0' || name[i] > '9') return 0;
            i++;
        }
        return 1;
    }
    return 0;
}

int is_course_folder(const char *name) {
    // Skip template and final pset folders
    if (strcmp(name, "pset_template") == 0 || 
        strcmp(name, "template") == 0 ||
        strcmp(name, "Final PSET") == 0 ||
        strcmp(name, "build") == 0 ||
        strcmp(name, "images") == 0) {
        return 0;
    }
    return 1; // Everything else is a course folder
}

int main() {
    char cwd[MAX_PATH];
    char course_path[MAX_PATH];
    char ps_path[MAX_PATH];
    char source[MAX_PATH];
    char dest_folder[MAX_PATH];
    char dest_file[MAX_PATH];
    char cmd[MAX_PATH * 2];
    
    getcwd(cwd, sizeof(cwd));
    
    // Create Final PSET folder if it doesn't exist
    snprintf(dest_folder, sizeof(dest_folder), "%s%cFinal PSET", cwd, PATH_SEP);
    #ifdef _WIN32
        mkdir(dest_folder);
    #else
        mkdir(dest_folder, 0755);
    #endif
    
    DIR *dir = opendir(cwd);
    struct dirent *entry;
    
    while ((entry = readdir(dir)) != NULL) {
        // Skip . and ..
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) continue;
        
        // Build full path to check if it's a directory
        snprintf(course_path, sizeof(course_path), "%s%c%s", cwd, PATH_SEP, entry->d_name);
        if (!is_directory(course_path)) continue;
        if (!is_course_folder(entry->d_name)) continue;
        
        // Found a course folder (Physics 225, Physics 180, etc.)
        DIR *course_dir = opendir(course_path);
        struct dirent *ps_entry;
        
        while ((ps_entry = readdir(course_dir)) != NULL) {
            // Skip . and ..
            if (strcmp(ps_entry->d_name, ".") == 0 || strcmp(ps_entry->d_name, "..") == 0) continue;
            
            // Build full path to check if it's a directory
            snprintf(ps_path, sizeof(ps_path), "%s%c%s", course_path, PATH_SEP, ps_entry->d_name);
            if (!is_directory(ps_path)) continue;
            if (!is_ps_folder(ps_entry->d_name)) continue;
            
            // Found a PS folder (PS1, PS2, etc.)
            snprintf(source, sizeof(source), "%s%cmain.pdf", ps_path, PATH_SEP);
            
            // Check if main.pdf exists
            FILE *f = fopen(source, "r");
            if (f) {
                fclose(f);
                
                // Use the FULL PS folder name
                snprintf(dest_file, sizeof(dest_file), "%s%c[%s] %s - %s.pdf", 
                        dest_folder, PATH_SEP, entry->d_name, ps_entry->d_name, USERNAME);
                
                // Copy the file
                #ifdef _WIN32
                    snprintf(cmd, sizeof(cmd), "copy \"%s\" \"%s\"", source, dest_file);
                #else
                    snprintf(cmd, sizeof(cmd), "cp \"%s\" \"%s\"", source, dest_file);
                #endif
                
                printf("Copying: %s -> %s\n", source, dest_file);
                system(cmd);
            }
        }
        closedir(course_dir);
    }
    closedir(dir);
    
    printf("\nDone! Check the 'Final PSET' folder.\n");
    return 0;
}

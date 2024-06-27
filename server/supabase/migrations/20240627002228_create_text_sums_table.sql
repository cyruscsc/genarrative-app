create table public.text_sums (
    id uuid default gen_random_uuid () primary key,
    title varchar,
    content text,
    summary text,
    created_by uuid references auth.users on delete cascade,
    created_at timestamp with time zone default now (),
    updated_at timestamp with time zone default now ()
);

create or replace trigger on_data_update
before update on public.text_sums
for each row execute procedure public.handle_data_update ();
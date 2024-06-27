create or replace function public.handle_data_update()
    returns trigger
    language plpgsql
    security definer
as $$
begin
    new.updated_at = now();
    return new;
end;
$$;